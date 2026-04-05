# System Health Monitor

A Python-based system monitoring tool that tracks CPU, memory and disk usage in real time, logs readings to a file, and flags anything above a defined threshold via a Flask dashboard.

## What it does

- Reads live CPU, memory and disk usage using psutil
- Flags readings that exceed defined thresholds (CPU > 80%, Memory > 75%, Disk > 85%)
- Logs every reading with a timestamp to a JSON file
- Displays live metrics and log history on a Flask dashboard
- Auto-refreshes every 5 seconds

## Tech Stack

- Python, Flask, psutil
- HTML/CSS (frontend)
- JSON logging
- Git

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Dashboard frontend |
| GET | `/metrics` | Get current system metrics |
| GET | `/logs` | Get full log history |

## Run Locally

1. Clone the repo
2. Install dependencies: `pip install flask psutil`
3. Run the app: `python app.py`
4. Open `http://127.0.0.1:5000` in your browser