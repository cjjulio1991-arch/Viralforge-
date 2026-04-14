from flask import Flask, jsonify
import json

app = Flask(__name__)

STATE_FILE = "state.json"

def load_state():
    try:
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    except:
        return {"status": "no data"}

@app.route("/")
def home():
    state = load_state()
    return f"""
    <h1>🧠 ViralForge Agent</h1>
    <p>Status: {state.get('status')}</p>
    <p>Cycles: {state.get('cycles')}</p>
    <p>Errors: {state.get('errors')}</p>
    <p>Last Run: {state.get('last_run')}</p>
    """

@app.route("/api")
def api():
    return jsonify(load_state())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
