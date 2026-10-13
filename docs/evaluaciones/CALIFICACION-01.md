# Retroalimentación — Laboratorio 1: Fundamentos, complejidad y recurrencias

**Estudiante:** Cristian José Méndez Guzmán · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-13 23:59 · **Versión revisada:** commit `448f468`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 25 |
| Calidad de la explicación teórica | 13 / 25 |
| Corrección de la implementación | 14 / 20 |
| Calidad del análisis de las gráficas | 14 / 20 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **69 / 100** |
| **Nota (0–5)** | **3.45** |

## 1. Corrección conceptual (19 / 25)
**Lo que hizo bien:**
- Distingue entre un resultado correcto y uno que llega a tiempo, y nombra la ventana de 4 horas como la restricción que no se cumple.
- Explica con números por qué un servidor el doble de rápido no basta: el trabajo crece 3.600 veces y la máquina solo lo reduce a la mitad.
- Calcula el consumo de energía por noche y por año, y lo compara con una alternativa más rápida.
- Reconoce que el orden de la lista decide a quién se llama primero.

**Lo que puede mejorar:**
- El ejemplo propio (la nómina) es muy breve: falta decir de dónde salen las 14 horas y qué datos se procesan.
- En la parte ética, el segundo perjuicio (los operadores) es débil; además el costo de los errores de la lista recae sobre todo en el paciente y no queda bien explicado quién más lo asume.
- Las 9 horas de consumo del servidor no se justifican.

## 2. Calidad de la explicación teórica (13 / 25)
**Lo que hizo bien:**
- Plantea la recurrencia de merge sort, identifica a=2, b=2 y f(n)=Θ(n), y concluye Θ(n log n) con el método maestro.
- Declara la predicción de los escenarios antes de medir y justifica que usaría el peor caso para decidir, por ser un sistema de salud.

**Lo que puede mejorar:**
- Las definiciones de peor, mejor y promedio no dicen sobre qué conjunto de entradas ni con qué tamaño fijo se toma el máximo, el mínimo o el promedio.
- Para insertion sort no se muestra cuántas veces se ejecuta cada línea del código: solo se suma el peor caso.
- Falta la tabla con la complejidad de cada algoritmo en el mejor caso, el peor caso y el caso promedio.
- La condición del método maestro se menciona pero no se verifica paso a paso.
- No se contrasta la predicción con el resultado ni se explica si el escenario B es de verdad el mejor caso.

## 3. Corrección de la implementación (14 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien de mayor a menor, no cambian la lista recibida, cuentan comparaciones entre elementos y no usan `sorted()` ni `sort()`.
- La mezcla de merge sort es propia y recursiva. Los generadores devuelven listas del tamaño pedido, sin repetidos y con semilla.

**Lo que puede mejorar:**
- `generar_casi_ordenado` mezcla posiciones al azar por toda la lista; el enunciado pedía un 98 % ordenado y un 2 % nuevo agregado al final.
- En `datos.py` faltan la descripción del módulo y las dos líneas en blanco entre funciones, y los docstrings no siguen el formato pedido.
- `_merge` no documenta sus parámetros ni lo que devuelve, y las funciones `ejecutar` de las partes 3 y 4 no tienen docstring.

## 4. Calidad del análisis de las gráficas (14 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes rotulados, leyenda y las curvas en los mismos ejes.
- Identifica correctamente el escenario C como el peor, el B como el mejor y el A como intermedio, y lo que dice coincide con las gráficas (por ejemplo, en n = 6400 el escenario C llega a unos 2,9 s y el A a unos 1,4 s).
- Responde lo del servidor con un dato medido y estima el tiempo para 1.200.000 registros, declarando el razonamiento de la extrapolación.

**Lo que puede mejorar:**
- El análisis de las gráficas se queda en descripciones generales; falta citar valores concretos.
- No explica qué pasa con los tamaños pequeños ni contrasta con detalle la gráfica con lo calculado en 4.1.
- El concepto técnico para la Secretaría es corto (menos de 400 palabras), no estima el tiempo de merge sort con un cálculo y no cita explícitamente la gráfica de la que sacó el dato.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- Siguió la estructura de carpetas acordada, el informe está en el orden pedido y las imágenes se ven con rutas relativas.
- Enlaza el código en las partes 3 y 4, incluye instrucciones para reproducir y tiene commits suficientes sobre el laboratorio.

**Lo que puede mejorar:**
- Se publicaron las carpetas `__pycache__` y `.vscode`; conviene excluirlas con un `.gitignore`.
- Las instrucciones mezclan rutas de Windows y de Mac/Linux y el enlace a `datos.py` y `algoritmos.py` podría ir donde se mencionan por primera vez.

## ¿El código funciona?
Sí. Ambos algoritmos ordenan bien listas pequeñas y aleatorias, y los scripts generan las gráficas sin errores.

## Para el próximo laboratorio
- Defina cada caso (peor, mejor, promedio) diciendo sobre qué entradas y qué tamaño se calcula.
- Muestre el conteo línea a línea y no olvide la tabla de complejidades.
- Siga al pie de la letra la especificación de los generadores de datos.
- Agregue docstrings a todas las funciones y revise PEP 8 (líneas en blanco entre funciones).
- Cite números concretos de sus gráficas y extienda el concepto técnico a la longitud pedida.
