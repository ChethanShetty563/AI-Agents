import random
from fastapi import FastAPI
import datetime

app = FastAPI()

DISK_LOGS = [
    "WARNING: Disk usage at 92% on /mnt/data",
    "INFO: Disk /dev/sda1 health status normal",
    "CRITICAL: Failed to write to disk, out of space on /var/log"
]

RAM_LOGS = [
    "INFO: Memory clearance routine completed successfully, freed 1.2GB",
    "WARNING: Physical memory usage exceeded 85%",
    "CRITICAL: Out of Memory (OOM) killer invoked in worker process"
]

CPU_LOGS = [
    "CRITICAL: CPU temperature peaked at 95C",
    "INFO: CPU voltage scaling normal",
    "WARNING: High CPU load average detected: 4.5 3.2 2.1"
]

NETWORK_LOGS = [
    "ERROR: Packet loss detected on interface eth0",
    "INFO: Network interface ens33 link up, 1000Mbps",
    "WARNING: High latency (200ms) detected to default gateway"
]

APP_LOGS = [
    "DEBUG: User session created for id=48912",
    "ERROR: Unhandled exception in payments module",
    "INFO: Scheduled database backup task initiated successfully"
]

@app.get("/logs")
def get_logs():
    timestamp = datetime.datetime.now().isoformat(timespec="seconds")
    return {
        "disk": f"[{timestamp}] {random.choice(DISK_LOGS)}",
        "ram": f"[{timestamp}] {random.choice(RAM_LOGS)}",
        "cpu": f"[{timestamp}] {random.choice(CPU_LOGS)}",
        "network": f"[{timestamp}] {random.choice(NETWORK_LOGS)}",
        "application": f"[{timestamp}] {random.choice(APP_LOGS)}"
    }
