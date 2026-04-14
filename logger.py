import os
from datetime import datetime

os.makedirs("output", exist_ok=True)

with open("output/log.txt", "a") as f:
    f.write(f"Run: {datetime.now()}\n")
