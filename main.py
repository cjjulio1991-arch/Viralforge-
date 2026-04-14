import time
from viral_engine import generate_posts
from optimize import rank_posts
from publish import send_all
from logger import log

INTERVALO = 300  # 5 minutos

def run_cycle():
    log("🚀 CICLO INICIADO")

    posts = generate_posts()
    top = rank_posts(posts)
    send_all(top)

    log("✅ CICLO COMPLETADO")

def main():
    while True:
        try:
            run_cycle()
            time.sleep(INTERVALO)

        except Exception as e:
            log(f"❌ ERROR: {e}")
            time.sleep(10)

if __name__ == "__main__":
    main()
