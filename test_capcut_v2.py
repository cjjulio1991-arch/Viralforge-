import os
from moviepy import ColorClip, TextClip, CompositeVideoClip

print("--- [ViralForge Engine v2.0] ---")

posibles_fuentes = ["fuente.ttf", "/system/fonts/Roboto-Regular.ttf", "/system/fonts/DroidSans.ttf"]
fuente_final = next((f for f in posibles_fuentes if os.path.exists(f)), None)

try:
    fondo = ColorClip(size=(720, 1280), color=(20, 20, 20), duration=5)
    if fuente_final:
        print(f"Usando fuente: {fuente_final}")
        texto = TextClip(
            text="AUTOMATIZACIÓN\nVIRAL", 
            font_size=70, 
            color='white', 
            font=fuente_final
        ).with_duration(5).with_position('center')
        video_final = CompositeVideoClip([fondo, texto])
    else:
        print("Aviso: No se encontró fuente, generando solo fondo.")
        video_final = fondo

    video_final.write_videofile("viral_video.mp4", fps=24, codec="libx264")
    print("\n[OK] ¡PROCESO EXITOSO!")
except Exception as e:
    print(f"Error: {e}")
