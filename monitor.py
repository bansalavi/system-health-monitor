import psutil
import datetime
import json

LOG_FILE = "health_log.json"

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 75
DISK_THRESHOLD = 85

def get_metrics():
    cpu = psutil.cpu_percent(interval=None)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    flagged = []
    if cpu > CPU_THRESHOLD:
        flagged.append("CPU")
    if memory > MEMORY_THRESHOLD:
        flagged.append("Memory")
    if disk > DISK_THRESHOLD:
        flagged.append("Disk")

    return {
        "timestamp": timestamp,
        "cpu": cpu,
        "memory": memory,
        "disk": disk,
        "flagged": flagged
    }

def log_metrics(metrics):
    try:
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(metrics)

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_logs():
    try:
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []