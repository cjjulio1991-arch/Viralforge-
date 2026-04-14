import random
from datetime import datetime
import os

hooks = [
    "Escucha esto 5 segundos:",
    "Si haces esto, cambias todo:",
    "Este error te está costando caro:"
]

body = [
    "Deja de esperar motivación. Empieza con disciplina.",
    "Rodéate de gente que te obligue a crecer.",
    "Haz lo difícil primero, siempre."
]

cta = [
    "Sígueme para más.",
    "Guarda este video.",
    "Compártelo con alguien."
]

script = f"""
🎬 REEL SCRIPT

HOOK:
{random.choice(hooks)}

CUERPO:
{random.choice(body)}

CTA:
{random.choice(cta)}

📅 {datetime.now()}
"""

os.makedirs("output/reels", exist_ok=True)
with open("output/reels/reel.txt", "w") as f:
    f.write(script)

print("Reel generado")
