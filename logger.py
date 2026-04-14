from datetime import datetime
import os

os.makedirs("logs", exist_ok=True)

def log(msg):
    line = f"{datetime.now().isoformat()} | {msg}"

    print(line)

    with open("logs/log.txt", "a") as f:
        f.write(line + "\n")
