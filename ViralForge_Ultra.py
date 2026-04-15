import os
import random
from gtts import gTTS
from moviepy import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip, concatenate_audioclips

print("--- [VIRALFORGE ULTRA: MODO FÁBRICA ACTIVADO] ---")

# CONFIGURACIÓN
fuente = "/system/fonts/Roboto-Regular.ttf"
carpeta_entrada = "./clips_crudos"
carpeta_salida = "./reels_listos"
frases_motivacionales = [
    "El éxito es la suma de pequeños esfuerzos.",
    "La disciplina te llevará donde la motivación no alcance.",
    "Crea tu propio camino con ViralForge."
]

# Crear carpetas si no existen
os.makedirs(carpeta_entrada, exist_ok=True)
os.makedirs(carpeta_salida, exist_ok=True)

def crear_voz_ia(texto, nombre_archivo):
    tts = gTTS(text=texto, lang='es')
    tts.save(nombre_archivo)
    return AudioFileClip(nombre_archivo)

def procesar_video(nombre_video, indice):
    try:
        print(f"\n>> Procesando clip {indice}: {nombre_video}")
        
        # 1. Carga de Video Base
        clip = VideoFileClip(os.path.join(carpeta_entrada, nombre_video)).subclipped(0, 6)
        
        # 2. Generar Voz de IA
        texto_ia = random.choice(frases_motivacionales)
        audio_voz = crear_voz_ia(texto_ia, f"voz_{indice}.mp3")
        
        # 3. Audio Final (Voz + Música si existe)
        musica_fondo = AudioFileClip("musica.mp3").with_duration(clip.duration).with_effects([lambda a: a.multiply_volume(0.2)])
        audio_final = CompositeAudioClip([audio_voz, musica_fondo])
        clip = clip.with_audio(audio_final)

        # 4. Texto con Transición (Efecto de escala)
        txt_clip = TextClip(
            text=texto_ia,
            font_size=50,
            color='yellow',
            font=fuente,
            method='caption',
            size=(clip.w*0.8, None)
        ).with_duration(clip.duration).with_position('center')
        
        # Efecto simple: Aparecer desde abajo
        txt_clip = txt_clip.with_start(0.5).with_effects([lambda c: c.with_position(lambda t: ('center', max(clip.h/2, clip.h - (t*200))))])

        # 5. Componer y Guardar
        video_final = CompositeVideoClip([clip, txt_clip])
        nombre_final = f"reel_viral_{indice}.mp4"
        video_final.write_videofile(os.path.join(carpeta_salida, nombre_final), fps=24, codec="libx264")
        
        print(f"[OK] Generado: {nombre_final}")

    except Exception as e:
        print(f"[ERROR en clip {indice}]: {e}")

# EJECUCIÓN MASIVA
archivos = [f for f in os.listdir(carpeta_entrada) if f.endswith('.mp4')]
if not archivos:
    print("¡No hay videos en ./clips_crudos! Mueve algunos videos ahí para empezar.")
else:
    for i, video in enumerate(archivos):
        procesar_video(video, i)
    print("\n--- [TRABAJO TERMINADO: REVISA LA CARPETA REELS_LISTOS] ---")
