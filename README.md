# VTube Studio Hotkey & Animation ID Finder

A simple Python utility for extracting **Hotkey IDs** from your currently loaded VTube Studio model. These IDs can be used in custom AI VTuber projects, automation scripts, Twitch integrations, and emotion/animation triggering systems.

## Features

* Connects directly to the VTube Studio Public API
* Uses **port 8006** by default
* Automatically requests and saves an authentication token
* Lists all available hotkeys for the current model
* Displays the corresponding Hotkey IDs
* Saves the authentication token for future use
* Lightweight and requires only one dependency

---

## Requirements

* Python 3.8+
* VTube Studio running
* API access enabled in VTube Studio
* VTube Studio API configured to use **port 8006**

### Install dependencies

```bash
pip install websocket-client
```

---

## VTube Studio API Port

This script is configured to connect to VTube Studio using:

```python
VTS_PORT = 8006
```

If your VTube Studio API uses a different port, edit the `VTS_PORT` variable near the top of `animationidfinderforvtubestudio.py`.

Example:

```python
VTS_PORT = 8001
```

---

## Setup

1. Open **VTube Studio**.
2. Ensure the **VTube Studio Public API** is enabled.
3. Verify that the API port is set to **8006**.
4. Load the model whose hotkeys/animations you want to inspect.
5. Place `animationidfinderforvtubestudio.py` in any folder.
6. Run the script:

```bash
python animationidfinderforvtubestudio.py
```

---

## First Run

On the first launch, the script will request an authentication token from VTube Studio.

When prompted in VTube Studio:

* Click **Allow**
* The script will create a file named:

```text
vts_token.json
```

This file stores your authentication token so you only have to authorize the script once.

After the token is saved, restart the script.

---

## Output

Once authenticated, the script will print all available hotkeys from the currently loaded model:

```text
Connected to VTube Studio...
Authenticated.

===== HOTKEY IDS =====

Happy -> 9fb9992e569f41bb98b7dc98b44e47a1
Angry -> d19056223bef4f838289d64fc323256f
Sad -> 8a477a3b550243dd913c7d9b87e00b9d
Thinking -> cd5dd5e85d5241fb9ad43dc8cf5ce90f
Neutral -> f9ce594f944e4ddbbe7e0ae9427122f4

Finished.
```

---

## Using the IDs

The extracted IDs can be used in your own VTube Studio projects:

```python
EMOTION_HOTKEYS = {
    "happy": "9fb9992e569f41bb98b7dc98b44e47a1",
    "angry": "d19056223bef4f838289d64fc323256f",
    "sad": "8a477a3b550243dd913c7d9b87e00b9d",
    "thinking": "cd5dd5e85d5241fb9ad43dc8cf5ce90f",
    "neutral": "f9ce594f944e4ddbbe7e0ae9427122f4",
}
```

You can then trigger these hotkeys through the VTube Studio Public API to activate:

* Expressions
* Emotions
* Animations
* Toggles
* Costume changes
* Other model actions

---

## Notes

* This tool only displays hotkeys for the **currently loaded model**.
* In VTube Studio, most animations and expressions are triggered through hotkeys.
* If you switch models, run the script again to obtain that model's hotkey IDs.
* Make sure VTube Studio is running and listening on **port 8006** before launching the script.

---

## License

This project is free to use and modify for personal and commercial VTuber projects.
