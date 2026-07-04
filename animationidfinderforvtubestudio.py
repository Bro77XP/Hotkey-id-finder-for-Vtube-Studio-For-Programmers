
import websocket
import json
import threading
import time
import os
import sys

VTS_PORT = 8006
TOKEN_FILE = "vts_token.json"


class HotkeyFinder:
    def __init__(self):
        self.url = f"ws://localhost:{VTS_PORT}"
        self.token = self.load_token()
        self.connect()

    def connect(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=lambda ws, e: print("Error:", e),
            on_close=lambda *args: print("Disconnected")
        )
        threading.Thread(target=self.ws.run_forever, daemon=True).start()

    def on_open(self, ws):
        print("Connected to VTube Studio...")
        time.sleep(0.5)

        if self.token:
            self.send({
                "apiName": "VTubeStudioPublicAPI",
                "apiVersion": "1.0",
                "requestID": "auth",
                "messageType": "AuthenticationRequest",
                "data": {
                    "pluginName": "Hotkey Finder",
                    "pluginDeveloper": "User",
                    "authenticationToken": self.token
                }
            })
        else:
            self.send({
                "apiName": "VTubeStudioPublicAPI",
                "apiVersion": "1.0",
                "requestID": "token",
                "messageType": "AuthenticationTokenRequest",
                "data": {
                    "pluginName": "Hotkey Finder",
                    "pluginDeveloper": "User"
                }
            })

    def on_message(self, ws, message):
        msg = json.loads(message)
        mtype = msg.get("messageType")

        if mtype == "AuthenticationTokenResponse":
            with open(TOKEN_FILE, "w") as f:
                json.dump(
                    {"token": msg["data"]["authenticationToken"]},
                    f
                )
            print("Token saved. Restart the script.")
            sys.exit()

        elif mtype == "AuthenticationResponse":
            print("Authenticated.\n")
            self.send({
                "apiName": "VTubeStudioPublicAPI",
                "apiVersion": "1.0",
                "requestID": "hotkeys",
                "messageType": "HotkeysInCurrentModelRequest"
            })

        elif mtype == "HotkeysInCurrentModelResponse":
            print("===== HOTKEY IDS =====\n")

            for hk in msg["data"]["availableHotkeys"]:
                print(
                    f"{hk['name']} -> {hk['hotkeyID']}"
                )

            print("\nFinished.")
            sys.exit()

    def send(self, data):
        if self.ws.sock and self.ws.sock.connected:
            self.ws.send(json.dumps(data))

    def load_token(self):
        if os.path.exists(TOKEN_FILE):
            with open(TOKEN_FILE) as f:
                return json.load(f).get("token")
        return None


if __name__ == "__main__":
    HotkeyFinder()

    while True:
        time.sleep(1)
