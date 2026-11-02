# Retroalimentación — Lab 03 Estructuras de datos

**Estudiante:** Cristian José Méndez Guzmán · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `0a662c4`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 17 / 20 |
| Calidad de la explicación teórica | 18 / 20 |
| Corrección de la implementación | 22 / 25 |
| Calidad del análisis de las gráficas | 21 / 25 |
| Documentación y organización del informe | 6 / 10 |
| **Total** | **84 / 100** |
| **Nota (0–5)** | **4.20** |

## 1. Corrección conceptual (17 / 20)
**Lo que hizo bien:**
- Explica bien por qué la tabla hash no sirve para rangos: la función hash destruye el orden.
- Estima la altura del árbol degenerado (cerca de 400.000) y sus comparaciones (cerca de 80.000 millones), y da la altura del árbol equilibrado (cerca de 19).
- Recomienda combinar tabla hash y árbol balanceado, y declara la estimación a 5.000.000 de envíos.

**Lo que puede mejorar (y cómo corregirlo):**
- Dice que las colisiones ocurren por el "principio del palomar" aunque haya más casillas que guías. Ese principio solo obliga a colisionar cuando hay más guías que casillas, así que no explica este caso.
  → *Cómo corregirlo:* piense por qué dos guías distintas pueden dar el mismo resto al dividir entre `m`, aunque `m` sea grande, y use el ejemplo 10, 24 y 17 con `m = 7`.
- No estima las comparaciones del árbol equilibrado, solo su altura.
  → *Cómo corregirlo:* relacione la altura con el número de inserciones y calcule el total aproximado de comparaciones para compararlo con el caso degenerado.
- La estimación de la tabla hash a 5.000.000 de envíos dice "exactamente los mismos microsegundos" y no da ninguna cifra. Además, no considera que una tabla más grande puede ser más lenta de recorrer.
  → *Cómo corregirlo:* tome un valor medido en su gráfica, dé una cifra aproximada y explique qué puede hacer que cambie con una tabla mucho más grande.

## 2. Calidad de la explicación teórica (18 / 20)
**Lo que hizo bien:**
- Justifica el `Θ(n)` de la lista y el `Θ(1 + α)` de la tabla.
- Nombra el supuesto de hash uniforme simple.
- Explica que, si todas las guías caen en una casilla, la tabla se vuelve una lista y cuesta `Θ(n)`.

**Lo que puede mejorar (y cómo corregirlo):**
- No explica por qué la longitud esperada de cada cadena es `α` ni qué significa "uniforme" para las guías.
  → *Cómo corregirlo:* añada una frase que diga con qué probabilidad cae una guía en cada casilla y cómo eso lleva a `n / m`.

## 3. Corrección de la implementación (22 / 25)
**Lo que hizo bien:**
- `ListaEnlazada` y `TablaHash` funcionan: búsquedas exitosas e infructuosas, colisión con `m = 7`, `factor_carga` y 20 colecciones aleatorias comparadas.
- La tabla reutiliza la lista y no usa `dict`, `set` ni `hash()`. La búsqueda de la lista usa un ciclo `while`.
- Los scripts `pruebas.py` y `medicion.py` corren sin errores.

**Lo que puede mejorar (y cómo corregirlo):**
- Faltan *docstrings* con `Args` y `Returns` en `generar_guias_inexistentes`, `experimento_a` y `experimento_b`, y estas dos últimas no tienen *type hints*. La clase `Nodo` tampoco tiene *docstring* y el de `ListaEnlazada` quedó incompleto.
  → *Cómo corregirlo:* añada a cada función un *docstring* Google-style con `Args` y `Returns`, y anote tipos (por ejemplo `-> None`).

## 4. Calidad del análisis de las gráficas (21 / 25)
**Lo que hizo bien:**
- Ambas gráficas existen, tienen título, ejes rotulados y leyenda. La primera usa seis valores de `n` con las dos curvas en los mismos ejes, y la segunda usa cuatro valores de `α`.
- Para la lista, pasar de `n = 10.000` a `n = 20.000` multiplica el tiempo por cerca de 2, y lo contrasta con `Θ(n)`. La lectura coincide con la gráfica.
- Reconoce que la tabla se ve plana y que el tiempo sube con `α`.

**Lo que puede mejorar (y cómo corregirlo):**
- No da valores leídos de las gráficas, solo descripciones generales. Para la tabla no calcula ningún factor de crecimiento.
  → *Cómo corregirlo:* lea de cada gráfica los valores de dos `n` consecutivos y divídalos para dar el factor de cada estructura.
- En la segunda gráfica, el punto de `α = 0,5` queda un poco más alto que el de `α = 1`, y el informe no lo menciona. Dice que el aumento es "100 % coherente" sin mostrar cifras.
  → *Cómo corregirlo:* cite los valores de la gráfica para `α` = 1, 4 y 10 y diga si el aumento es proporcional a `α`. Mencione también el ruido de la medición.

## 5. Documentación y organización del informe (6 / 10)
**Lo que hizo bien:**
- El `README.md` sigue el orden pedido, incluye su nombre, enlaza el código en cada parte y muestra las dos gráficas con ruta que sí resuelve.
- Hay cinco commits con mensajes descriptivos para el laboratorio.

**Lo que puede mejorar (y cómo corregirlo):**
- No siguió la estructura de carpetas acordada: los archivos del laboratorio están sueltos dentro de `laboratorios/` en vez de en `laboratorios/lab3-estructuras-datos/`.
  → *Cómo corregirlo:* cree esa carpeta y mueva allí `README.md`, `estructuras.py`, `pruebas.py`, `medicion.py` y `graficas/` con `git mv`.
- Las instrucciones de reproducción mandan a hacer `cd laboratorios/lab3-estructuras-datos`, una carpeta que no existe, y usan una ruta de Windows para activar el entorno.
  → *Cómo corregirlo:* una vez movida la carpeta, revise cada comando en una terminal nueva e indique también cómo activar el entorno en Mac y Linux.
- Hay archivos generados (`__pycache__/`, `.vscode/`) publicados en el repositorio del laboratorio 1.
  → *Cómo corregirlo:* agréguelos a `.gitignore` y quítelos del seguimiento.

## ¿El código funciona?
Sí. Las pruebas pasan y la medición corre completa y genera las dos gráficas. Las estructuras devuelven los mismos resultados.
