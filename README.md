# ARNAB_BOT website demo

A responsive green/black Flask dashboard. Start and Stop operate in demo mode only;
no game API calls, account credentials, or friend requests are made.

## Run locally
```bash
python -m venv .venv
# activate the environment, then:
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000

## Deploy
Push this folder to a Git repository and create a web service on Render using
the included `render.yaml`.
