import requests
import json
import os
import time

WEBHOOK_URL = "https://hook.us2.make.com/8ty344qqh8rqd51qlc8cyjmx7wf7ixn7"
QUEUE_FILE = "queue.json"


def load_queue():
    if not os.path.exists(QUEUE_FILE):
        return []
    with open(QUEUE_FILE, "r") as f:
        return json.load(f)


def save_queue(queue):
    with open(QUEUE_FILE, "w") as f:
        json.dump(queue, f)


def send_post(post, post_id):
    try:
        r = requests.post(WEBHOOK_URL, json={
            "post": post,
            "id": post_id
        }, timeout=10)

        return r.status_code

    except Exception as e:
        print(f"Error envío: {e}")
        return None


def send_all(posts):
    queue = load_queue()

    # agregar nuevos posts a cola
    for i, post in enumerate(posts):
        queue.append({"id": i, "post": post})

    save_queue(queue)

    # intentar enviar todo
    new_queue = []

    for item in queue:
        status = send_post(item["post"], item["id"])

        if status == 200:
            print(f"Enviado OK | {item['id']}")
        else:
            print(f"Fallo {status} | reintento luego")
            new_queue.append(item)

        time.sleep(1)

    save_queue(new_queue)

    print(f"Pendientes en cola: {len(new_queue)}")
