import os
import random
from gtts import gTTS
from moviepy import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip, CompositeAudioClip

print("--- [VIRALFORGE ULTRA v2: INTELIGENCIA ELÁSTICA] ---")

fuente = "/system/fonts/Roboto-Regular.ttf"
carpeta_entrada = "./clips_crudos"
carpeta_salida = "./reels_listos"
frases = [
    "La disciplina vence a la inteligencia.",
    "No cuentes los días, haz que los días cuenten.",
    "El éxito requiere sacrificios.",
    "Sé el cambio que quieres ver en el mundo."
]

os.makedirs(carpeta_salida, exist_ok=True)

def crear_voz_ia(texto, archivo_audio):
    tts = gTTS(text=texto, lang='es')
    tts.save(archivo_audio)
    return AudioFileClip(archivo_audio)

videos = [f for f in os.listdir(carpeta_entrada) if f.endswith('.mp4')]

if not videos:
    print("No hay videos en clips_crudos.")
else:
    for i, nombre in enumerate(videos):
        try:
            print(f"\n>> Procesando {i}: {nombre}")
            ruta = os.path.join(carpeta_entrada, nombre)
            
            # CARGA INTELIGENTE: Si el video es corto, no lo corta
            clip_original = VideoFileClip(ruta)
            duracion_final = min(clip_original.duration, 6) # Máximo 6 segundos
            clip = clip_original.subclipped(0, duracion_final)
            
            # VOZ Y MÚSICA
            frase = random.choice(frases)
            audio_voz = crear_voz_ia(frase, f"temp_voz.mp3")
            
            # Cargamos música con volumen bajo (0.1)
            musica = AudioFileClip("musica.mp3").with_duration(clip.duration).with_volume_scaled(0.1)
            audio_final = CompositeAudioClip([audio_voz, musica])
            clip = clip.with_audio(audio_final)

            # TEXTO ADAPTADO
            txt = TextClip(
                text=frase,
                font_size=40,
                color='yellow',
                font=fuente,
                method='caption',
                size=(clip.w * 0.8, None)
            ).with_duration(clip.duration).with_position('center')

            # COMPOSICIÓN
            final = CompositeVideoClip([clip, txt])
            final.write_videofile(os.path.join(carpeta_salida, f"viral_{i}.mp4"), fps=24, codec="libx264")
            
            # Limpieza de archivos temporales de voz
            audio_voz.close()
            
        except Exception as e:
            print(f"[ERROR]: {e}")

print("\n--- FÁBRICA FINALIZADA ---")
