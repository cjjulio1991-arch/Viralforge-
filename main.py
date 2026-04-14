import json
import os
from datetime import datetime

STATE_FILE = "state.json"


def load_state():
    if not os.path.exists(STATE_FILE):
        return {
            "status": "idle",
            "cycles": 0,
            "errors": 0,
            "last_run": None
        }

    try:
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    except:
        return {
            "status": "error",
            "cycles": 0,
            "errors": 1,
            "last_run": None
        }


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=4)


def update_state(status="running", error=False):
    state = load_state()

    state["status"] = status
    state["cycles"] += 1
    state["last_run"] = str(datetime.now())

    if error:
        state["errors"] += 1

    save_state(state)
