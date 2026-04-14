from datetime import datetime

with open("output/log.txt", "a") as f:
    f.write(f"Run: {datetime.now()}\n")
