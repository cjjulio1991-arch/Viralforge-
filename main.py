import os
from moviepy import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip

print("--- [ViralForge Engine: MODO PRO] ---")

# Archivos que ya tienes en la carpeta
video_input = "video_base.mp4"
audio_input = "musica.mp3"
fuente = "/system/fonts/Roboto-Regular.ttf"

try:
    # 1. Cargar video y cortarlo a 7 segundos para que sea rápido
    print("Cargando video base...")
    clip = VideoFileClip(video_input).subclipped(0, 7)
    
    # 2. Cargar audio y ajustarlo al tiempo del video
    print("Sincronizando música...")
    musica = AudioFileClip(audio_input).with_duration(clip.duration)
    clip = clip.with_audio(musica)

    # 3. Crear texto (Marca de agua)
    print("Añadiendo texto...")
    texto = TextClip(
        text="HECHO CON VIRALFORGE\n@jof-hiel",
        font_size=50,
        color='white',
        font=fuente if os.path.exists(fuente) else "Arial"
    ).with_duration(7).with_position(('center', 800))

    # 4. Mezclar todo
    final = CompositeVideoClip([clip, texto])

    # 5. Exportar
    print("Renderizando Reel Final...")
    final.write_videofile("REEL_TERMINADO.mp4", fps=24, codec="libx264", audio_codec="aac")
    
    print("\n[OK] ¡PROCESO EXITOSO! El archivo es: REEL_TERMINADO.mp4")

except Exception as e:
    print(f"\n[ERROR]: {e}")
