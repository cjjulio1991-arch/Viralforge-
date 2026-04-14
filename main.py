from viral_engine import generate_posts
from optimize import rank_posts
from publish import send_all
from logger import log

def main():
    log("🚀 AGENTE INICIADO")

    # 1. generar contenido
    posts = generate_posts()

    # 2. optimizar / rankear
    top_posts = rank_posts(posts)

    # 3. publicar
    send_all(top_posts)

    log("✅ PROCESO COMPLETADO")


if __name__ == "__main__":
    main()
