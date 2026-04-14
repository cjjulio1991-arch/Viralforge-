from flask import Flask, render_template_string
import json
import os

app = Flask(__name__)

STATE_FILE = "state.json"
QUEUE_FILE = "queue.json"


def load_json(file, default):
    if not os.path.exists(file):
        return default
    with open(file, "r") as f:
        return json.load(f)


@app.route("/")
def home():
    state = load_json(STATE_FILE, {
        "status": "idle",
        "cycles": 0,
        "errors": 0,
        "last_run": None
    })

    queue = load_json(QUEUE_FILE, [])

    html = f"""
    <h1>🚀 ViralForge Dashboard PRO</h1>

    <h2>Estado del Agente</h2>
    <p>Status: {state['status']}</p>
    <p>Cycles: {state['cycles']}</p>
    <p>Errors: {state['errors']}</p>
    <p>Last Run: {state['last_run']}</p>

    <h2>📦 Cola de Envío</h2>
    <p>Posts pendientes: {len(queue)}</p>

    <ul>
    {''.join([f"<li>{q['post'][:60]}...</li>" for q in queue])}
    </ul>
    """

    return render_template_string(html)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
