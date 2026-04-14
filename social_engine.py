from datetime import datetime
import random

hooks = [
    "Nadie te dice esto:",
    "Esto cambia tu mentalidad:",
    "Si sigues así, nunca avanzarás:"
]

messages = [
    "Disciplina > motivación.",
    "Tu entorno define tu futuro.",
    "El éxito es repetición diaria."
]

post = f"""
🔥 {random.choice(hooks)}

{random.choice(messages)}

#motivacion #mentalidad #exito

{datetime.now()}
"""

with open("output/post.txt", "w") as f:
    f.write(post)

print("Post listo para publicar")
