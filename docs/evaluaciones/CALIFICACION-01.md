# Retroalimentación — Fundamentos, complejidad y recurrencias

**Estudiante:** Cristian Jose Mendez Guzman · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-06 23:59 · **Versión revisada:** commit `5408820`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 9 / 25 |
| Calidad de la explicación teórica | 0 / 25 |
| Corrección de la implementación | 12 / 20 |
| Calidad del análisis de las gráficas | 7 / 20 |
| Documentación y organización del informe | 3 / 10 |
| **Total** | **31 / 100** |
| **Nota (0–5)** | **1.55** |

## 1. Corrección conceptual (9 / 25)
**Lo que hizo bien:**
- Distingue que insertion sort ordena bien pero no alcanza a terminar en la ventana de 4 horas.
- Explica que duplicar la velocidad del servidor no sirve, porque el algoritmo crece de forma cuadrática (60 veces más datos son unas 3.600 veces más operaciones).
- Menciona dos perjuicios (pacientes críticos sin llamar y operadores llamando sin prioridad) e indica quién asume el costo.

**Lo que puede mejorar:**
- Falta el segundo ejemplo propio, distinto de Tamiza, con datos aproximados y la restricción que se incumple.
- La parte ambiental es una sola frase: falta explicar cómo el tiempo se vuelve energía y por qué pesa al repetirse cada madrugada durante años.
- No se discute la obligación que impone el hecho de que el orden de la lista decida a quién se llama primero.
- Las respuestas son muy breves y no desarrollan cada requisito de las Partes 1 y 2.

## 2. Calidad de la explicación teórica (0 / 25)
**Lo que puede mejorar:**
- El informe no tiene la Parte 3.1: faltan las definiciones de peor caso, mejor caso y caso promedio, cuál usaría para decidir y la predicción antes de medir.
- No tiene la Parte 4.1: faltan la recurrencia de merge sort, su solución paso a paso, el cálculo línea a línea de insertion sort y la tabla de complejidades.

## 3. Corrección de la implementación (12 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien de mayor a menor, no cambian la lista recibida y cuentan comparaciones entre elementos (probados con listas aleatorias y casos pequeños). `merge_sort` tiene su propia mezcla recursiva.
- Los tres generadores dan listas del tamaño pedido, sin repetidos, y con semilla.
- El código no tiene problemas de estilo en longitud de línea ni en nombres.

**Lo que puede mejorar:**
- Los generadores `generar_casi_ordenado` y `generar_inverso` usan `sorted()`. La guía prohíbe usarlo; debía construir el orden con su propio código.
- Faltan docstrings completos (con Args y Returns) en los generadores, y `ejecutar` y `_merge` casi no los tienen. `ejecutar` tampoco tiene *type hints* en sus variables internas.

## 4. Calidad del análisis de las gráficas (7 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen y tienen título, ejes rotulados, leyenda y las curvas pedidas en los mismos ejes. Se ve bien que el escenario C es el más lento, el B el más rápido y que merge sort le gana a insertion sort al crecer n.
- Recomienda merge sort y rechaza la compra del servidor.

**Lo que puede mejorar:**
- Las gráficas no están incrustadas en el informe, y no hay análisis de la Parte 3.2 (peor, mejor y promedio) ni de la Parte 4.2 (qué hace cada curva y si coincide con la teoría).
- La extrapolación a 1.200.000 registros no explica su razonamiento ni se declara como estimación, y las cifras no concuerdan con sus mediciones: con 2,2 s para 6.400 datos, insertion sort tardaría muchas más horas que las 4,8 indicadas.
- El dato que respalda la respuesta sobre el servidor no cita la gráfica ni el tamaño medido.
- Faltan consideraciones distintas del tiempo (memoria, estabilidad, mantenimiento).

## 5. Documentación y organización del informe (3 / 10)
**Lo que hizo bien:**
- El laboratorio está en `laboratorios/lab1-fundamentos-complejidad-recurrencias/`, ubicación válida, con los archivos y gráficas del entregable.

**Lo que puede mejorar:**
- No hay enlaces a `algoritmos.py`, `datos.py`, `parte3_casos.py` ni `parte4_complejidad.py` en el informe.
- Las instrucciones de reproducción están incompletas (solo el primer paso, y sin el comando para cada parte).
- Hay menos de cinco commits sobre el laboratorio (tres) y el último no es muy descriptivo.
- Se publicaron carpetas que no van en el repositorio: `__pycache__/` y `.vscode/`; debían ir en `.gitignore`.

## ¿El código funciona?
Sí. Los dos algoritmos ordenan bien, y los dos scripts corren sin errores y generan las gráficas.

## Para el próximo laboratorio
- Completar todas las partes del informe en el orden pedido, desarrollando cada requisito de la guía.
- Incrustar las gráficas con ruta relativa y analizar lo que muestran.
- Escribir el desarrollo de la recurrencia y el cálculo línea a línea, aunque sea sencillo.
- Extrapolar con la forma de la curva y declarar que es una estimación.
- Agregar `__pycache__/` y `.vscode/` al `.gitignore` y hacer commits pequeños y descriptivos.
