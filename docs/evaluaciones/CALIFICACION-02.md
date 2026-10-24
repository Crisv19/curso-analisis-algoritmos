# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Cristian José Méndez Guzmán · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `339bb45`

Buen trabajo: el código funciona y el informe está bien encaminado.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 15 / 20 |
| Calidad de la explicación teórica | 17 / 20 |
| Corrección de la implementación | 20 / 25 |
| Calidad del análisis de las gráficas | 19 / 25 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **80 / 100** |
| **Nota (0–5)** | **4.00** |

## 1. Corrección conceptual (15 / 20)
**Lo que hizo bien:**
- Explica bien por qué dividir no ayuda a hallar el máximo de un arreglo: combinar cuesta O(1) y el resultado sigue siendo O(n).
- Recomienda divide y vencerás y declara que lo del millón de registros es una estimación.

**Lo que puede mejorar:**
- En "Tamaños pequeños" dice que la ventaja empieza entre n=50 y n=100, pero no muestra ningún dato medido que lo sostenga.
- En la estimación para 1.000.000 usa un tiempo "a modo de ejemplo" (0,5 s) en vez de citar con claridad su medición, y el "menos de 3 segundos" de divide y vencerás no tiene cálculo que lo respalde.

## 2. Calidad de la explicación teórica (17 / 20)
**Lo que hizo bien:**
- Plantea T(n) = 2T(n/2) + Θ(n), explica de dónde sale cada término y verifica el Caso 2 del método maestro comparando con n^(log₂2) = n.

**Lo que puede mejorar:**
- La justificación del Θ(n²) de la fuerza bruta es muy breve: falta mostrar cuántos pares se prueban (aprox. n(n+1)/2).

## 3. Corrección de la implementación (20 / 25)
**Lo que hizo bien:**
- Las tres funciones están bien hechas, el caso cruzado es correcto y no se llama a la fuerza bruta desde divide y vencerás.
- Las pruebas cubren todos los casos pedidos y 20 listas aleatorias; todas pasan.

**Lo que puede mejorar:**
- Faltan líneas en blanco entre funciones (PEP 8) en `subarreglo.py` (después del docstring inicial) y en `medicion.py`.
- `ejecutar_experimento` en `medicion.py` no tiene type hints ni docstring (solo las pruebas están exentas).

## 4. Calidad del análisis de las gráficas (19 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda, ambas curvas en los mismos ejes y 7 tamaños (de 10 a 4000).
- Dice que de 2000 a 4000 la fuerza bruta se multiplica casi por 4 y divide y vencerás por poco más de 2; esto es coherente con la gráfica (fuerza bruta de unos 0,15 s a unos 0,55 s).

**Lo que puede mejorar:**
- No calcula el factor con números concretos: debía mostrar los tiempos leídos y la división.
- No indica si repitió las mediciones.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- Estructura correcta (`laboratorios/lab2-divide-y-vencer/`), orden del informe, enlaces al código y gráfica visible.
- Hay varios commits descriptivos del laboratorio.

**Lo que puede mejorar:**
- Las instrucciones para activar el entorno solo sirven en Windows; conviene indicar también el comando para Mac/Linux.
- Quedaron publicados `__pycache__/` y `.vscode/` del Laboratorio 1; use un `.gitignore` bien guardado (el actual parece tener una codificación extraña) para evitarlo. No descuenta puntos.

## ¿El código funciona?
Sí. Las pruebas pasan, la medición corre completa y genera la gráfica. Los resultados de ambos algoritmos coinciden.

## Para el próximo laboratorio
- Respalde cada afirmación con valores medidos: ponga una tabla con los tiempos y calcule los factores a mano.
- En la estimación a gran escala use sus propias mediciones, no un número de ejemplo.
- Justifique cada Θ contando operaciones (por ejemplo, el número de pares).
- Revise PEP 8 (dos líneas en blanco entre funciones) y ponga type hints y docstring en todas las funciones que no sean pruebas.
- Repita las mediciones y dígalo en el informe.
