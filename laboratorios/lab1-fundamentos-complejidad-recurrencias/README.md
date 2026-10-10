# Laboratorio Evaluativo 01 — Fundamentos, Complejidad y Recurrencias

**Autor:** Cristian Jose Mendez Guzman  
**Fecha:** Octubre 2026  

---

## Instrucciones de Reproducción

Para ejecutar los experimentos y ver las gráficas, abre la terminal en la carpeta principal del repositorio y usa estos comandos:

1. **Activar el entorno virtual**: `..\venv\Scripts\activate` (o `source venv/bin/activate` en Unix).
2. **Instalar dependencias**: `pip install -r requirements.txt`
3. **Entrar a la carpeta del lab**: `cd laboratorios/lab1-fundamentos-complejidad-recurrencias`
4. **Correr Parte 3 (Casos)**: `python parte3_casos.py`
5. **Correr Parte 4 (Tiempo)**: `python parte4_complejidad.py`

---

## Parte 1 — Analizar el algoritmo antes de comprar hardware

Un algoritmo puede dar el resultado correcto (como Tamiza, que sí ordena bien la lista), pero ser inviable en la práctica porque no cumple con las restricciones de tiempo. En este caso, no logra procesar 1.200.000 registros en la ventana estricta de 4 horas.

Comprar un servidor el doble de rápido no sirve de nada. Como *Insertion Sort* tiene una complejidad de $O(n^2)$, si pasamos de 20.000 a 1.200.000 datos (60 veces más), las operaciones crecen al cuadrado: $60^2 = 3.600$ veces más trabajo. Tener un procesador que vaya al doble de velocidad solo reduce el tiempo a la mitad, lo cual no hace ni cosquillas frente a un aumento de 3.600 veces.

**Ejemplo propio:** Un sistema para calcular la nómina de 80.000 empleados. Si se hace con un algoritmo $O(n^2)$ usando bucles anidados, podría tardar 14 horas. Aunque los pagos calculados sean exactos, el algoritmo es inviable porque no logra enviar el archivo al banco antes de las 6:00 a.m. para pagarles el mismo día.

---

## Parte 2 — Responsabilidad ambiental y ética

**En lo ambiental:**  
Un servidor corriendo *Insertion Sort* a tope durante 9 horas consume mucha energía: unos $4,05\text{ kWh}$ por noche ($1.478\text{ kWh}$ al año). Si cambiamos a un algoritmo que termine en 15 minutos, el consumo anual cae a solo $41\text{ kWh}$. No optimizar el código es literalmente botar energía y dinero.

**En lo ético:**  
Que el algoritmo sea lento afecta a personas reales:
1. **Pacientes graves ignorados:** Como el sistema se corta a las 6:00 a.m., los pacientes con más riesgo quedan por fuera. Ese costo en salud lo pagan **el paciente y su familia**.
2. **Operadores perdiendo el tiempo:** El call center termina llamando a gente que no es prioridad. Ese costo operativo lo asume **la Secretaría de Salud**.

Como esto es un triaje médico, el orden de la lista decide quién vive y quién espera. Hacer un algoritmo rápido y exacto es una obligación ética.

---

## Parte 3 — Peor caso, mejor caso y caso promedio

**Enlaces al código:** [algoritmos.py](algoritmos.py) | [datos.py](datos.py) | [parte3_casos.py](parte3_casos.py)

### 3.1 — Explicación y Predicción
- **Peor caso ($O(n^2)$):** El máximo de operaciones que puede hacer el algoritmo (lista al revés).
- **Mejor caso ($\Omega(n)$):** El mínimo de operaciones que puede hacer (lista ya ordenada).
- **Caso promedio ($\Theta(n^2)$):** El promedio de operaciones probando todas las combinaciones posibles.

Para autorizar el paso a producción me baso en el **peor caso**. En salud no podemos jugar a la suerte; si el algoritmo cumple el tiempo en el peor escenario posible, nunca va a fallar en producción.

**Predicción antes de medir:**
- **Escenario C (Inverso):** Peor caso.
- **Escenario A (Aleatorio):** Caso promedio.
- **Escenario B (Casi ordenado):** Mejor caso.

### 3.2 — Análisis de las gráficas

![Comparaciones Insertion Sort](graficas/parte3_comparaciones.png)
![Tiempo Insertion Sort](graficas/parte3_tiempo.png)

*Análisis:* Las gráficas salieron tal como dice la teoría.  
- La curva verde (Escenario C) es el peor caso y forma una parábola completa ($n^2/2$).  
- La curva azul (Escenario A) es el caso promedio; también crece como parábola pero hace más o menos la mitad de operaciones.
- La curva naranja (Escenario B) es el mejor caso y se ve casi plana (lineal $\Omega(n)$). *Insertion Sort* solo es rápido si le das los datos ya ordenados.

---

## Parte 4 — Complejidad y recomendación técnica

**Enlace al código:** [parte4_complejidad.py](parte4_complejidad.py)

### 4.1 — Cálculo Teórico

**Merge Sort (Método Maestro):**
El algoritmo se divide en $a=2$ subproblemas de tamaño $n/2$ ($b=2$) y luego los une en tiempo $\Theta(n)$.
La ecuación es:
$$T(n) = 2T(n/2) + \Theta(n)$$
Calculamos $n^{\log_2 2} = n^1 = n$. Como la función $f(n) = \Theta(n)$ crece igual que $n$, cae en el **Caso 2** del Método Maestro. La complejidad es **$\Theta(n \log n)$**.

**Insertion Sort (Línea a línea):**
El bucle de afuera hace $n-1$ pasos y el de adentro hace $i$ pasos en el peor de los casos (orden inverso). La suma es:
$$\sum_{i=1}^{n-1} i = \frac{n(n-1)}{2} = \frac{n^2 - n}{2}$$
Lo que nos da una complejidad de **$\Theta(n^2)$**.

### 4.2 — Validación Experimental

![Comparación de Tiempo](graficas/parte4_tiempo.png)

*Análisis:* La gráfica es súper clara. *Merge Sort* (línea de abajo) casi no sube aunque haya más datos, gracias a que es $\Theta(n \log n)$. En cambio, *Insertion Sort* (línea de arriba) se dispara rapidísimo formando una curva pronunciada, confirmando que es $O(n^2)$.

### 4.3 — Concepto Técnico para la Secretaría de Salud

1. **Recomendación:** Cambiar de inmediato a **Merge Sort**. En la vida real no podemos confiar en que los datos nos van a llegar siempre ordenados.
2. **Estimación para 1.200.000 registros:** Usando mis datos medidos ($2,2\text{ segundos}$ para $6.400$ registros), hice esta estimación matemática:
   - Los datos crecen $187.5$ veces ($1.200.000 / 6.400$).
   - Para *Insertion Sort* ($O(n^2)$), el tiempo crece al cuadrado. Sería $2,2\text{ s} \times (187.5)^2 \approx 77.343\text{ segundos}$, es decir, unas **~21,5 horas**. Totalmente inviable.
   - *Merge Sort* ($O(n \log n)$) lo resolvería en unos pocos segundos.
3. **Sobre el hardware:** **No compren el servidor**. Un servidor el doble de rápido solo bajaría el tiempo de *Insertion Sort* a 10,7 horas. El problema es el código, no la máquina.
4. **Otras consideraciones:** *Merge Sort* gasta un poquito más de RAM (unos $10\text{ MB}$), pero hoy en día eso no es nada. Además es estable, así que respeta el orden de llegada de los pacientes que tengan el mismo riesgo.