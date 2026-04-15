import os
from moviepy import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip

print("--- [ViralForge PRO: Video + Audio + Texto] ---")

# Rutas de archivos
fuente = "/system/fonts/Roboto-Regular.ttf"
video_input = "video_base.mp4"
audio_input = "musica.mp3"

try:
    # 1. Cargar el video y cortarlo (primeros 5 segundos)
    clip_fondo = VideoFileClip(video_input).subclipped(0, 5)
    
    # 2. Cargar el audio y ajustarlo a la duración del video
    musica = AudioFileClip(audio_input).with_duration(clip_fondo.duration)
    video_con_audio = clip_fondo.with_audio(musica)

    # 3. Crear el texto superpuesto
    texto = TextClip(
        text="CONTENIDO AUTOMATIZADO\n@jof-hiel", 
        font_size=50, 
        color='white', 
        font=fuente,
        stroke_color='black',
        stroke_width=2
    ).with_duration(5).with_position('center')

    # 4. Montaje final
    final_reel = CompositeVideoClip([video_con_audio, texto])

    # 5. Exportar con calidad para Instagram/FB
    print("Renderizando Reel Pro...")
    final_reel.write_videofile("reel_final.mp4", fps=24, codec="libx264", audio_codec="aac")
    
    print("\n[OK] ¡REEL GENERADO EXITOSAMENTE!")

except Exception as e:
    print(f"Error en el proceso: {e}")
