# Clonación de voz (gratis)

Usa **Chatterbox Multilingual** (Resemble AI, licencia MIT): gratis, de código abierto, se puede usar en videos comerciales y habla español.

## Instalación (una vez por sesión)

```bash
python3 -m venv ~/voz-venv
~/voz-venv/bin/pip install chatterbox-tts "setuptools<81"
```

El modelo se descarga de Hugging Face la primera vez (pesa unos 3 GB). El entorno de la nube `edici-n-de-video` ya tiene esos sitios permitidos.

## Uso

```bash
~/voz-venv/bin/python -I herramientas/voz/clonar.py "Recuerda, sé positivo." salida.wav referencia.wav
```

- `referencia.wav`: de 10 a 30 segundos de la voz del usuario, limpia: sin música, sin otras voces y sin eco.
- En CPU tarda unos 15–25 s por frase corta.
- Cada audio lleva una marca de agua inaudible (Perth) que lo identifica como generado por IA.

## Regla de uso

La voz clonada se usa **solo con autorización del usuario en el chat**, para frases sueltas como un gancho o el cierre "sé positivo". El resto del video es siempre su voz real.
