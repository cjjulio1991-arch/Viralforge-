from datetime import datetime
import random, os

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
for i in range(10):  # genera 10 opciones
    p = f"""
🔥 {random.choice(hooks)}

{random.choice(messages)}

👉 {random.choice(cta)}

{random.choice(hashtags_pool)}

{datetime.now()}
"""
    candidatos.append((score(p), p))

# ordena por score y guarda top 3
top = sorted(candidatos, key=lambda x: x[0], reverse=True)[:3]

for i, (_, post) in enumerate(top):
    with open(f"output/post_{i}.txt", "w") as f:
        f.write(post)

print("Top 3 posts generados (ULTRA)")
