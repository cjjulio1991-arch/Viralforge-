import requests

WEBHOOK_URL = "https://hook.us2.make.com/8ty344qqh8rqd51qlc8cyjmx7wf7ixn7"

def send_all(posts):
    """
    Envía todos los posts al webhook (Make / Zapier / API).
    """

    if not posts:
        print("No hay posts para enviar")
        return

    for i, post in enumerate(posts):
        try:
            response = requests.post(WEBHOOK_URL, json={
                "id": i,
                "post": post
            })

            print(f"Enviado post {i} | status: {response.status_code}")

        except Exception as e:
            print(f"Error enviando post {i}: {e}")
