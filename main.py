import time
import json
import os
from datetime import datetime

from viral_engine import generate_posts
from optimize import rank_posts
from publish import send_all
from logger import log

INTERVALO = 300
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


def run_cycle():
    try:
        update_state("running")

        log("🚀 CICLO INICIADO")

        posts = generate_posts(10)
        log(f"Posts generados: {len(posts)}")

        top = rank_posts(posts)
        log(f"Top seleccionados: {len(top)}")

        send_all(top)

        update_state("running")
        log("✅ CICLO COMPLETADO")

    except Exception as e:
        update_state("error", error=True)
        log(f"❌ ERROR EN CICLO: {e}")


def main():
    while True:
        run_cycle()
        time.sleep(INTERVALO)


if __name__ == "__main__":
    main()

