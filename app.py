import os
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/api/start")
def start():
    data = request.get_json(silent=True) or {}
    uid = str(data.get("uid", "")).strip()
    duration = int(data.get("duration", 10))
    if not uid:
        return jsonify(ok=False, message="Enter a UID first."), 400
    if duration < 1 or duration > 60:
        return jsonify(ok=False, message="Duration must be 1–60 minutes."), 400
    # Safe demo only: no external requests or game actions are performed.
    return jsonify(ok=True, message=f"Demo started for UID {uid} ({duration} min).")

@app.post("/api/stop")
def stop():
    return jsonify(ok=True, message="Demo stopped.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
