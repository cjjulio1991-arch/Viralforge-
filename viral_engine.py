from datetime import datetime
import random
import os

hooks = [
    "Nadie te dice esto, pero es la verdad:",
    "Si supieras esto antes, tu vida sería diferente:",
    "Esto te está robando el éxito sin que lo notes:",
    "El 90% falla por esto:",
    "Lee esto antes de rendirte:"
]

messages = [
    "La disciplina gana cuando la motivación desaparece.",
    "No es falta de tiempo, es falta de prioridad.",
    "Si no cambias hoy, repetirás tu vida un año más.",
    "El éxito es aburrido, por eso pocos lo logran.",
    "Tu entorno define tu futuro más de lo que crees."
]

def generate_post():
    content = f"""
🔥 VIRAL POST

{random.choice(hooks)}

{random.choice(messages)}

📅 {datetime.now()}
"""
    return content

def generate_posts(n=10):
    os.makedirs("output", exist_ok=True)

    posts = []
    for i in range(n):
        post = generate_post()
        posts.append(post)

        with open(f"output/viral_{i}.txt", "w") as f:
            f.write(post)

    return posts
