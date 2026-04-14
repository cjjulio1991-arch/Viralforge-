from datetime import datetime
import random, os
import requests

hooks = [
    "Nadie te dice esto:",
    "El 90% falla por esto:",
    "Si sigues así, nunca avanzarás:",
    "Esto te está frenando:",
    "Lee esto antes de rendirte:",
    "Te mintieron sobre esto:"
]

messages = [
    "Disciplina > motivación.",
    "Tu entorno define tu futuro.",
    "El éxito es repetición diaria.",
    "Si no cambias hoy, repites tu vida.",
    "Haz lo difícil ahora y vive fácil después.",
    "Lo que haces hoy decide tu año."
]

cta = [
    "Sígueme para más.",
    "Guarda esto.",
    "Compártelo.",
    "Aplica esto hoy.",
    "Comenta 'voy' si empiezas hoy."
]

hashtags_pool = [
    "#motivacion #exito #mentalidad",
    "#dinero #disciplina #emprender",
    "#habitos #productividad #vida",
    "#negocios #riqueza #mindset"
]

def score(post):
    s = 0
    if "🔥" in post: s += 1
    if "?" in post or "esto" in post.lower(): s += 1
    if "👉" in post: s += 1
    if "#" in post: s += 1
    return s

os.makedirs("output", exist_ok=True)

candidatos = []

# generar 10 opciones
for i in range(10):
    p = f"""
🔥 {random.choice(hooks)}

{random.choice(messages)}

👉 {random.choice(cta)}

{random.choice(hashtags_pool)}

{datetime.now()}
"""
    candidatos.append((score(p), p))

# ordenar y elegir top 3
top = sorted(candidatos, key=lambda x: x[0], reverse=True)[:3]

webhook_url = "https://hook.us2.make.com/8ty344qqh8rqd51qlc8cyjmx7wf7ixn7"

# guardar y enviar cada post
for i, (_, post) in enumerate(top):
    with open(f"output/post_{i}.txt", "w") as f:
        f.write(post)

    # enviar a Make
    requests.post(webhook_url, json={
        "post": post,
        "id": i
    })

print("Top 3 posts generados y enviados 🚀") 
