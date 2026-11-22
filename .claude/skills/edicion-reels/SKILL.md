---
name: edicion-reels
description: Guía obligatoria para editar CUALQUIER video del usuario (reels verticales 9:16, con su voz, sin música, a 1.3x, que cierran con "SÉ POSITIVO"). Úsala siempre que el usuario pida editar, cortar, recortar o montar un video, o cuando suba videos crudos a Google Drive para editarlos.
---

# Cómo usar esta guía

- Sigue **toda** la guía de abajo en cada video, sin excepción, salvo que el usuario pida otra cosa en el chat.
- **En sesiones en la nube** (sin acceso a la PC):
  - Los crudos llegan por **Google Drive**. Descárgalos con el conector de Drive a `edicion_v12/work/` y trabaja con ffmpeg.
  - El motor de la PC (`engine.py`, `style2.py`, `reel.py`, `icons2.py`, `analyze.py`, `track.py`, `tile.py`) **no está en este repositorio**. Si no está, recrea los pasos con ffmpeg y Python siguiendo las mismas reglas.
  - Los SFX están en este repo, en `skills/brag/assets/sfx/` (es la misma carpeta que en la PC está en `~/.claude/plugins-src/edici-n-de-video-main/skills/brag/assets/sfx/`).
  - **Gancho débil:** se pregunta al usuario antes de cambiarlo (sección 2.2). Nunca se cambia por cuenta propia.
  - **Drive:** no se sube nada salvo que el usuario lo pida (sección 1).

# Guía de edición — Reels verticales

Esta guía es la estructura base para editar **todos** los videos. Sale de las referencias (`videos de referencia/`) y del feedback del usuario. Se actualizó por última vez el 22-nov-2026.

El estilo visual aprobado es **Video 1 v3** (`edicion_v12/output/Video1_EsteAnoSi_EDITADO_v3.mp4`), con las **reglas nuevas de esta versión**: sin música, velocidad 1.3x, verificación de labios y gancho.

> **Reglas de oro**
> 1. **SIN MÚSICA. Volumen de música = 0.** Solo voz y efectos de sonido suaves.
> 2. **Solo se escucha la voz del presentador.** Ninguna otra voz de fondo.
> 3. **Todo el video se acelera a 1.3x.**
> 4. **Estructura fija:** GANCHO → MENSAJE / ESTRUCTURA → CTA → **"SÉ POSITIVO"**.
> 5. **Una sola cosa fuerte en pantalla a la vez.** La persona siempre sabe a dónde mirar.

---

## 0. Antes de editar: entender el contenido

Antes de cortar nada hay que **ver y entender todo el video crudo**:
- Leer la transcripción completa, con tiempos por palabra.
- Identificar **de qué habla**: el tema, la idea central, la metáfora o historia que usa, y el mensaje que quiere dejar.
- Preguntarse **cómo puede impactar más a la gente**: cuál es la frase más fuerte, cuál es el dolor y cuál es la solución.
- Con eso se arma el guion final (sección 2). El video tiene que ser **coherente y tener sentido completo**: cada frase lleva a la siguiente, sin saltos raros ni ideas cortadas.

---

## 1. Formato de salida

| Parámetro | Valor |
|---|---|
| Resolución | 1080×1920 (vertical 9:16) |
| FPS | 30 |
| **Velocidad** | **1.3x en todo el video** (imagen y voz). La voz se acelera **sin cambiar el tono** (`atempo=1.3`), así no suena aguda |
| Códec | H.264, CRF 17, `yuv420p`, `+faststart` |
| Audio | AAC 256 kbps, 44.1 kHz estéreo |
| **Música** | **0 % — NO SE PONE MÚSICA** |
| Volumen de la VOZ | Normalizado a -14 LUFS, el estándar de Reels/TikTok. Esto es el volumen de **la voz y los efectos**, NO de música |
| Duración final | **30–60 s ya acelerado a 1.3x** (versión corta). La versión completa, solo si la pide |
| Drive | **No se sube nada a Drive salvo que el usuario lo pida.** Si lo pide, la carpeta es "Videos Editados - Reels". Desde aquí solo se pueden subir archivos de hasta 10 MB, así que va una copia 1080p en HEVC con 2 pasadas por debajo de 7 MB y se avisa que el original pesado está en `output/` |

Las carpetas son `videos crudos/` (entrada), `edicion_v12/` (motor y scripts), `edicion_v12/output/` (finales) y `edicion_v12/work/` (temporales).

---

## 2. Estructura del video (SIEMPRE)

| # | Parte | Qué es | Duración aprox. (ya a 1.3x) |
|---|---|---|---|
| 1 | **GANCHO** | Frase motivadora, disruptiva o una pregunta que haga que la persona **se quede**. Es lo primero que se escucha | 0–3 s |
| 2 | **MENSAJE** | El problema o dolor y la idea, con suspenso | 10–20 s |
| 3 | **ESTRUCTURA** | La explicación: historia, metáfora, pasos o la solución concreta | 10–25 s |
| 4 | **CTA** | Llamado a la acción: comenta, comparte, guarda o sígueme | 2–5 s |
| 5 | **"SÉ POSITIVO"** | Cierre obligatorio, **siempre después del CTA** | 1–2 s |

### 2.1 Si NO dice "sé positivo"
Si en el crudo no hay ninguna toma suya diciendo "recuerda, sé positivo", **igual se cierra con "SÉ POSITIVO"**, pero en imagen:
- Una tarjeta final a pantalla completa (fondo oscuro elegante, texto crema grande "SÉ POSITIVO") de 1.5 a 2 s.
- O el texto grande "SÉ / POSITIVO" sobre su última toma, si queda bien.
- Lleva su SFX de cierre (`interface/bong_001.ogg` a 0.18).

### 2.2 Gancho débil → PEDIR AUTORIZACIÓN ANTES
Si al revisar el contenido el gancho **no es bueno**, porque no es atractivo, no genera curiosidad o la persona se va a ir:
1. **No cambiarlo por cuenta propia.** Primero se le pregunta al usuario.
2. Decirle claro: *"Tu gancho no es tan fuerte por X. Te propongo hacer Y."*
3. Propuestas posibles, para que elija:
   - **Extracto adelantado (teaser):** poner al inicio, durante 2–4 s, la frase más fuerte o impactante de **su propio video** (por ejemplo, el giro o la conclusión) y después arrancar el video normal.
   - **Gancho visual:** una imagen o animación generada por código, o una imagen generada con IA si hay herramienta disponible, con una pregunta o dato disruptivo en texto grande.
   - **Combinar** el teaser con la imagen.
4. Solo se aplica **cuando el usuario lo autoriza**.

---

## 3. Guion y cortes (revisar CADA corte y CADA palabra)

### 3.1 Solo SU voz: nadie más habla en el video
En los crudos suele haber **otras voces de fondo**: el apuntador que le lee el guion, alguien del equipo o comentarios ("me repites", "a ver", "dale", "una, dos, tres"). **Ninguna de esas voces puede salir en el video**, salvo que el usuario mande un guion o avise explícitamente que habrá otras personas hablando y cómo quiere editarlas.

Se verifican **dos cosas** en cada frase que se usa:
1. **Volumen:** su micrófono suena a -20/-30 dB y las voces de fondo a -35/-50 dB. Las líneas bajas se descartan.
2. **Labios (verificación visual):** como no se puede escuchar, hay que **comprobar en la imagen que él está moviendo la boca** en ese tramo.
   - Se mide el movimiento de la zona de la boca (región inferior de la cara detectada) cuadro a cuadro durante cada frase elegida.
   - Si hay voz pero **la boca no se mueve**, esa voz **no es suya**: se descarta o se corta ese tramo.
   - También se revisa con hojas de contacto: tiene que verse hablando en las frases usadas.
3. Si una frase **solo existe en la voz de otra persona** (por ejemplo, el apuntador la dijo y él no la repitió bien), **no se usa**. Se busca una toma suya que diga lo mismo.
4. Hay que descartar también las tomas donde **no está en cuadro** (entrando o saliendo) o está de espaldas.

### 3.2 Sin repeticiones y con sentido
- **Nunca repetir la misma frase** dos veces, ni una toma corta repetida. Él suele grabar varias tomas de la misma frase: **se elige UNA sola**, normalmente la última completa y limpia.
- El orden final tiene que **contar una historia coherente**. Hay que leer el guion final de corrido y confirmar que se entiende y tiene sentido de principio a fin.
- No dejar frases cortadas a la mitad ni ideas que quedan colgadas.

### 3.3 Puntos de corte: que no se coma palabras ni deje pausas
- La marca de tiempo de Whisper **puede fallar por 50–150 ms**. No se corta con ella a ciegas.
- Cada inicio y cada final se **ajusta al silencio real**: buscar el mínimo de energía (ventanas de 10 ms) en ±0.3 s alrededor del borde. Antes del corte tiene que haber menos de -55 dB.
- Hay que verificar cada unión: la energía 40 ms antes y 40 ms después.
- Cada pieza lleva un micro-fundido de 12 ms de entrada y 20 ms de salida.
- **Cuando deja de hablar, se corta.** Las pausas de más de 0.4 s dentro de una toma se eliminan.
- Si habla de corrido sin pausa en el punto de corte, se mueve el corte a la pausa natural más cercana, aunque entre una palabra más. Es mejor eso que una palabra mocha.

### 3.4 Muletillas (fuera)
- Quitar "y mira", "mira", "ya", "este", "o sea", "eh", "bro", "hermano", "a ver", "dale", "una, dos, tres", "es más", las repeticiones y los arranques en falso.
- Si una muletilla está **pegada** a la palabra siguiente sin silencio, se busca otra toma de esa frase. Si no hay, se deja, porque una palabra mocha es peor.
- Para detectar muletillas o voces que Whisper no transcribe, buscar tramos con voz (más de -38 dB) sin palabra asignada, de más de 0.15 s, y revisarlos.

---

## 4. Velocidad 1.3x

- **Todo** el video final va a **1.3x**: imagen y voz.
- Voz: `atempo=1.3`, que acelera sin cambiar el tono.
- Imagen: `setpts=PTS/1.3`, manteniendo 30 fps de salida.
- Los tiempos de textos, gráficos, cortes y SFX **se calculan sobre el video ya acelerado**.
- La forma más limpia es acelerar el corte intermedio (`cutN.mp4` y `cutN.wav`) **antes** de renderizar. Así la transcripción y los tiempos se escalan ÷1.3 y todo cuadra.
- Las duraciones mínimas de la guía (textos de ≥1.2 s, imágenes de ~2 s) son **en tiempo final**, ya acelerado.

---

## 5. Cámara y encuadre

- **Nada de recentrar de golpe.** La cámara queda **fija en cada toma**, con un acercamiento muy lento (+3 % a lo largo de la toma).
- Los cambios de tamaño de plano se hacen **con CORTES**, nunca con zooms animados ni saltos.
- **No hace falta estar perfectamente centrado.** Basta con que se vean la cara y las manos.
  - Zona libre: la cara puede estar entre el 30 % y el 70 % del ancho, y entre el 30 % y el 48 % del alto.
  - Si se sale de esa zona, hay un paneo **lento** (τ ≈ 0.9 s, ≤ ~1.5 px por cuadro).
- El encuadre inicial de cada toma pone la cara al 50 % del ancho y al 40 % del alto.
- **Tamaños de plano** (zoom sobre el crudo 4K vertical):

  | Plano | Zoom | Uso |
  |---|---|---|
  | W (abierto) | 1.10 | Contexto; cuerpo casi entero |
  | M (medio) | 1.24 | Base, de cintura para arriba |
  | C (cerrado) | 1.48 | Énfasis y emoción |

- Se **alternan** los planos y nunca van dos iguales seguidos. En tomas de más de 2.5 s se hace un **corte interno** de plano en una palabra clave.
- Rastreo de la cara a 5 fps con **doble filtro anti-falsos**:
  - **Global:** se descartan las caras con una altura o un tamaño muy distintos a la mediana del video.
  - **Local:** mediana móvil de ±1.5 s.

---

## 6. Subtítulos (siempre presentes)

Son sobrios, en blanco y negro:

| Parámetro | Valor |
|---|---|
| Fuente | Montserrat 700, 48 px |
| Caja | Negra redondeada (radio 14), opacidad ~80 %, padding 26×16 |
| Palabras dichas / por decir | Blanco / gris (150,150,150) |
| Posición | Centrado, y ≈ 1470 (bajo, lejos de la cara) |
| Bloque | Máximo 4 palabras / 22 caracteres; se corta en fin de frase, en pausas y en cada corte |
| Escritura | Normal (no todo en mayúsculas), **con la ortografía corregida** ("sé positivo", "y adivina"…) |

- **Sin colores, sin brillos y sin rebotes.**
- **Se ocultan mientras hay un texto grande.** Las palabras resaltadas salen del subtítulo y pasan al texto grande.

---

## 7. Texto grande (palabras resaltadas)

| Parámetro | Valor |
|---|---|
| Fuente | Montserrat 900, MAYÚSCULAS |
| Color | **Crema (243, 224, 198)**, un solo color, sin contorno ni brillo; solo una sombra suave |
| Tamaño | 110–150 px; **se ajusta solo para no pasar de 960 px de ancho** |
| Posición | Tercio superior (centro y ≈ 330), **detrás de la persona**. Nunca tapa la cara |
| Animación | Cada línea aparece cuando la dice: sube 26 px con un fundido de 0.18 s |
| Duración | Mínimo ~1.2–1.5 s (en tiempo final). Nunca se encima con el siguiente texto grande |
| Frecuencia | ~1 por toma o menos, solo en las ideas clave |

---

## 8. Apoyos visuales (imágenes, íconos, animaciones)

Sirven para transmitir el mensaje **no solo de forma auditiva sino visual**, y para que la persona se quede enganchada.

### 8.1 Duración y permanencia
- **Cada imagen o gráfico dura cerca de 2 s como mínimo** (en tiempo final, ya a 1.3x). Si dura menos, no se nota.
- **Si sigue hablando del mismo tema, la imagen SE QUEDA** en pantalla mientras dure ese tema: a un lado o de fondo, "observándose", para reforzar visualmente lo que dice. Se quita cuando cambia de idea.
- Entran con un **pop** (0.45 → 1, 0.3 s) y quedan con una respiración suave (±2 %).

### 8.2 Tipos
1. **Íconos animados por código** (230–330 px, a un lado: x ≈ 830, y ≈ 600–640): batería que se descarga, calendario, reloj, crecimiento, check, X, advertencia, ciclo, portapapeles, celular, fuego, volante, bote, faro, globo de comentario, etc. Se crean nuevos según el tema.
2. **Flechas y objetos dibujados**: flechas, diana, barras de progreso, contadores, píldoras de texto.
3. **Pantalla completa animada por código** (1.5–3 s): tarjeta con degradado, cuadrícula y viñeta, con una mini-animación del concepto (iceberg, carretera, faro, contador, tachado, etc.). El subtítulo sigue visible encima. Se usa una por video para el concepto principal.
4. **Foto B-roll a pantalla completa** (zoom lento 1.00 → 1.10, ~2 s o lo que dure la frase): solo libres de derechos (Wikimedia Commons, con licencia anotada). Máximo 1–2 por video.
5. **Imagen generada con IA**: solo si hay una herramienta disponible y aporta al mensaje.

### 8.3 Qué NO hacer
- Apilar texto grande, ícono y foto al mismo tiempo.
- Gráficos de menos de ~2 s.
- Colores chillones o neón.
- Tapar la cara.

---

## 9. Color y transiciones

- Gradación suave: saturación ×1.05, contraste ×1.06 y viñeta ligera.
- Tramo del problema desaturado al 30 %; vuelve al color normal en el giro.
- **Sin barridos (whip) ni destellos.**
- Final: fundido a oscuro en los últimos 0.5 s, **después** de "SÉ POSITIVO".

---

## 10. Audio

### 10.1 Voz: lo más importante
- Filtro paso alto de 70 Hz, compresor (umbral 0.1, ratio 3) y ganancia ×1.35.
- Velocidad 1.3x con `atempo` (sin cambiar el tono).
- Normalización final del total (voz + SFX) con `loudnorm` a I=-14 LUFS, TP=-1.5, y luego un limitador.

### 10.2 Música: **NO SE USA**
- **Volumen de música = 0.** No se agrega ninguna pista musical.
- En el código, `MUSIC_LEVEL = 0.0` en `reel.py` (con 0 el mezclador omite la música).
- Solo se cambia si el usuario lo pide de forma explícita en el chat.

### 10.3 Efectos de sonido (SFX): uno por cada cosa que aparece, suaves
| Evento | Sonido | Volumen |
|---|---|---|
| 1.ª línea de un texto grande | swoosh suave | 0.16 |
| Líneas siguientes | `casino/card-slide-1.ogg` | 0.22 |
| Ícono o gráfico que cae | `interface/drop_002.ogg` | 0.30 |
| Foto o pantalla completa | swoosh 0.20 + `casino/card-place-1.ogg` 0.30 | — |
| Giro de la idea | `impact/impactSoft_heavy_001.ogg` | 0.22 |
| "Sé positivo" | `interface/bong_001.ogg` | 0.18 |

Los SFX están en `~/.claude/plugins-src/edici-n-de-video-main/skills/brag/assets/sfx/`.

---

## 11. Flujo de trabajo (paso a paso)

1. **Transcribir** (faster-whisper `medium`, español, marcas por palabra) → `work/tN.json`.
2. **Entender el contenido** (sección 0) y evaluar el gancho. **Si es débil, preguntar al usuario antes de seguir** (sección 2.2).
3. **Medir el volumen por línea** (`analyze.py N`) y **verificar los labios** en las frases candidatas, para usar solo su voz.
4. **Rastrear la cara** (`track.py N`).
5. **Escribir `vN.py`**:
   - `RAW`: una sola toma por frase, sin repeticiones, en orden coherente.
   - `INNER_CUTS`.
   - `build()`: textos e imágenes que se quedan mientras dura el tema.
   - Cierre con "sé positivo", con su voz o con la tarjeta de imagen.
6. Ajustar los bordes al silencio y quitar las pausas internas (`snap_segs` + `split_silences`). Verificar las uniones.
7. `python vN.py cut` → corte intermedio, **acelerado a 1.3x**.
8. `python vN.py stills …` + `tile.py` → **revisar los fotogramas**: él hablando en cada frase, nada tapa la cara, textos dentro del ancho.
9. `python vN.py render` → video final.
10. **Verificar**:
    - hoja de contacto a 2 fps;
    - energía en cada corte;
    - -14 LUFS;
    - **sin música**;
    - duración de 30–60 s;
    - termina con "SÉ POSITIVO".
11. Entregar en `output/` y anotar en `NOTAS.txt` qué se cortó, qué se descartó (voces de fondo) y qué hay que revisar.

Motor: `edicion_v12/engine.py` + `style2.py` + `reel.py` + `icons2.py`.

---

## 12. Checklist antes de entregar

- [ ] **Sin música (0 %).**
- [ ] **Solo su voz**: volumen y labios verificados; ninguna voz de fondo.
- [ ] **Acelerado a 1.3x**, con la voz en su tono natural.
- [ ] Gancho fuerte en los primeros 3 s (si era débil, se consultó al usuario).
- [ ] Estructura: gancho → mensaje → estructura → CTA → **SÉ POSITIVO**.
- [ ] Ninguna frase repetida; el guion se entiende y tiene sentido completo.
- [ ] Ninguna palabra cortada, sin muletillas y sin pausas muertas.
- [ ] La cámara nunca salta; cara y manos visibles; planos alternados.
- [ ] Subtítulos B/N con la ortografía corregida, ocultos bajo los textos grandes.
- [ ] Una sola cosa fuerte en pantalla a la vez.
- [ ] Imágenes de ~2 s como mínimo, que se quedan mientras sigue el tema, con SFX suave.
- [ ] Textos grandes dentro del ancho y sin tapar la cara.
- [ ] -14 LUFS (voz + SFX).
- [ ] Créditos de las fotos anotados.
