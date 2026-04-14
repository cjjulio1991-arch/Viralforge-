from datetime import datetime
import random
import os

hooks = [
    "Nadie te dice esto:",
    "El 90% falla por esto:",
    "Si sigues así, nunca avanzarás:",
    "Esto te está frenando:",
    "Lee esto antes de rendirte:"
]

messages = [
    "Disciplina > motivación.",
    "Tu entorno define tu futuro.",
    "El éxito es repetición diaria.",
    "Si no cambias hoy, repites tu vida.",
    "Haz lo difícil ahora y vive fácil después."
]

cta = [
    "Sígueme para más.",
    "Guarda esto.",
    "Compártelo.",
    "Aplica esto hoy."
]

hashtags = [
    "#motivacion #exito #mentalidad",
    "#dinero #disciplina #emprender",
    "#habitos #productividad #vida",
]

# Crear carpeta si no existe
os.makedirs("output", exist_ok=True)

# Generar múltiples posts
for i in range(3):
    post = f"""
🔥 {random.choice(hooks)}

{random.choice(messages)}

👉 {random.choice(cta)}

{random.choice(hashtags)}

{datetime.now()}
"""
    filename = f"output/post_{i}.txt"
    
    with open(filename, "w") as f:
        f.write(post)

print("3 posts virales generados")
