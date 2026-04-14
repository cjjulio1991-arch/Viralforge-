import time
import json
from datetime import datetime

from viral_engine import generate_posts
from optimize import rank_posts
from publish import send_all
from logger import log

INTERVALO = 300

STATE_FILE = "state.json"

def load_state():
    try:
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    except:
        return {"status": "idle", "cycles": 0, "errors": 0}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=4)

def run_cycle(state):
    log("🚀 CICLO INICIADO")

    posts = generate_posts()
    top = rank_posts(posts)
    send_all(top)

    state["cycles"] += 1
    state["last_run"] = datetime.now().isoformat()
    state["status"] = "running"

    log("✅ CICLO COMPLETADO")

def main():
    state = load_state()

    while True:
        try:
            run_cycle(state)
            save_state(state)
            time.sleep(INTERVALO)

        except Exception as e:
            state["errors"] += 1
            state["status"] = "error"
            save_state(state)

            log(f"❌ ERROR: {e}")
            time.sleep(10)

if __name__ == "__main__":
    main()
