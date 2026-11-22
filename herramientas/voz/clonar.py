"""Genera voz en español con Chatterbox Multilingual.
Uso: python clonar.py "texto" salida.wav [referencia.wav]
"""
import sys, time, torch, torchaudio
from chatterbox.mtl_tts import ChatterboxMultilingualTTS

texto, salida = sys.argv[1], sys.argv[2]
ref = sys.argv[3] if len(sys.argv) > 3 else None
t = time.time()
modelo = ChatterboxMultilingualTTS.from_pretrained(device="cpu")
print(f"modelo cargado en {time.time()-t:.0f}s", flush=True)
t = time.time()
wav = modelo.generate(texto, language_id="es", audio_prompt_path=ref,
                      exaggeration=0.5, cfg_weight=0.5)
torchaudio.save(salida, wav, modelo.sr)
print(f"audio generado en {time.time()-t:.0f}s -> {salida}")
