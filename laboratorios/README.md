\# Laboratorio Evaluativo 03 — Estructuras de datos



\*\*Autor:\*\* Cristian Jose Mendez Guzman  

\*\*Fecha:\*\* Octubre 2026



\---



\## 1. Instrucciones de Reproducción



Para ejecutar los experimentos y generar las gráficas, abre la terminal en la raíz del repositorio y usa estos comandos:



1\. \*\*Activar el entorno virtual\*\*: `..\\venv\\Scripts\\activate`

2\. \*\*Navegar a la carpeta del laboratorio\*\*: `cd laboratorios/lab3-estructuras-datos`

3\. \*\*Ejecutar casos de prueba (sin errores significa éxito)\*\*: `python pruebas.py`

4\. \*\*Ejecutar mediciones y generar gráficas\*\*: `python medicion.py`



\---



\## Parte 1 — Verificación de las estructuras



\*\*Enlaces al código:\*\* \[estructuras.py](estructuras.py) | \[pruebas.py](pruebas.py)



Para verificar las estructuras, implementé aserciones (`assert`) que evaluaron búsquedas exitosas e infructuosas. Validé la colisión forzada instanciando una tabla con $m=7$ e insertando las guías 10, 24 y 17 (cuyo módulo 7 es 3 en todos los casos). Comprobé que las tres guías se insertaron correctamente, que la lista de la casilla 3 alcanzó un tamaño de 3 nodos y que el factor de carga quedó en $3/7$. Finalmente, validé con 20 colecciones aleatorias que ambas estructuras devolvieran siempre el mismo resultado para guías existentes e inexistentes.



\---



\## Parte 2 — Medición y Gráfica



\*\*Enlace al código:\*\* \[medicion.py](medicion.py)



!\[Lista vs Tabla](graficas/lista\_vs\_tabla.png)



!\[Tiempo vs Alfa](graficas/tiempo\_vs\_alfa.png)



\*Nota metodológica:\* En el \*\*Experimento A\*\*, medí 6 tamaños de $n$ (desde 100 hasta 20.000). Usé números primos para $m$ cercanos a $n/2$ para mantener el factor de carga $\\alpha \\approx 2$. En el \*\*Experimento B\*\*, fijé $n=20.000$ y varié $m$ usando primos específicos (39989, 19997, 5003, 1999) para lograr factores de carga $\\alpha$ de $0.5, 1, 4$ y $10$. Para cada punto de ambas gráficas promedié el tiempo de 200 búsquedas inexistentes medidas con `time.perf\_counter()`.



\---



\## Parte 3 — Análisis 



\### 1. Costo teórico

Buscar una guía inexistente en una Lista Enlazada cuesta $\\Theta(n)$ porque, como no hay índice ni orden, el algoritmo está obligado a revisar cada uno de los $n$ elementos hasta toparse con el final de la lista. En la Tabla Hash con encadenamiento, el costo promedio es $\\Theta(1 + \\alpha)$: se gasta $\\Theta(1)$ calculando la función hash para llegar al cajón, y luego se recorre una lista corta de tamaño esperado $\\alpha$ (donde $\\alpha = n/m$). 

Este costo se basa en el \*\*supuesto de hash uniforme simple\*\*, el cual asume que la función reparte las claves de manera perfectamente pareja entre todos los cajones. Si este supuesto falla y todas las guías caen en la misma casilla, la tabla colapsa, convirtiéndose esencialmente en una única lista enlazada larga y su tiempo de búsqueda empeora a $\\Theta(n)$.



\### 2. Lo medido contra lo esperado

En la primera gráfica, al pasar de $n=10.000$ a $n=20.000$ (se duplica la entrada), el tiempo de la Lista Enlazada se multiplicó por $\\approx 2$, lo cual confirma su crecimiento lineal $\\Theta(n)$. Por otro lado, la curva de la Tabla Hash se mantuvo completamente plana al duplicar $n$, confirmando el comportamiento $\\Theta(1)$ constante (dado que mantuvimos $\\alpha \\approx 2$).

En la segunda gráfica (Experimento B), al mantener $n$ fijo y aumentar $\\alpha$ progresivamente desde $0.5$ hasta $10$, el tiempo de búsqueda creció de forma lineal. Esto es 100% coherente con la teoría $\\Theta(1 + \\alpha)$: a medida que hay menos cajones para la misma cantidad de guías, las cadenas dentro de cada cajón se hacen más largas y lentas de recorrer.



\### 3. Explique las colisiones

Una colisión ocurre cuando dos o más guías distintas arrojan el mismo resultado al pasar por la función hash, terminando en la misma casilla. Esto sucede por el principio del palomar (o la paradoja del cumpleaños): aunque haya más casillas que guías, la probabilidad de que dos caigan al azar en el mismo hueco es muy alta.

\- \*\*Encadenamiento:\*\* Resuelve la colisión guardando una lista enlazada en cada casilla. Si varias guías caen allí (como 10, 24 y 17 cayendo en la casilla 3 con $m=7$), simplemente se agregan a la lista de ese cajón. \*Ventaja:\* No se satura ni falla si hay muchas guías. \*Costo:\* Requiere memoria adicional para los punteros de los nodos.

\- \*\*Direccionamiento abierto:\*\* Guarda todo directamente en el arreglo. Si la casilla está llena, salta a otra siguiendo una secuencia (como el sondeo lineal). \*Ventaja:\* Ahorra memoria al no usar punteros. \*Costo:\* Sufre agrupamientos primarios y se vuelve lentísimo si la tabla se llena demasiado (requiriendo redimensionarla).



\### 4. Tabla hash o árbol de búsqueda

Para el monitoreo por rango ("guías entre X y Y"), \*\*la tabla hash no sirve\*\*. La función hash destruye cualquier orden aritmético: saber dónde quedó la guía 3000 no da ninguna pista de dónde está la 3001, obligando a recorrer toda la tabla en $\\Theta(m+n)$.

Un \*\*Árbol de Búsqueda Binario (BST)\*\* sí sirve, porque su propiedad mantiene las claves ordenadas: el recorrido en orden extrae los rangos eficientemente en $\\Theta(h + k)$ (donde $k$ son los resultados). Sin embargo, si las 400.000 guías llegaran \*\*ya ordenadas\*\*, un BST normal se deformaría colgando todo hacia la derecha, convirtiéndose en una lista. Su altura $h$ sería casi $400.000$ ($\\Theta(n)$) y armarlo costaría unas astronómicas $400.000^2 / 2 \\approx 80.000.000.000$ comparaciones. Si usáramos un árbol equilibrado (como AVL), su altura se mantendría en $\\log\_2(400.000) \\approx 19$, haciendo que las consultas sean rapidísimas ($\\Theta(\\log n)$).



\### 5. Concepto para la jefa de operaciones

Recomiendo utilizar una \*\*combinación de ambas\*\*: una \*\*Tabla Hash\*\* para absorber las miles de consultas puntuales del call center en tiempo $\\Theta(1)$, y sincronizar los datos diarios hacia un \*\*Árbol Balanceado\*\* para que el área de operaciones saque sus reportes por rango sin problemas de degeneración.

\*Estimación para 5.000.000 de envíos (búsqueda inexistente):\* 

Asumiendo que con $n=20.000$ la Lista Enlazada tardó $\\approx 0.001$ segundos, al escalar $250$ veces la entrada ($5.000.000 / 20.000 = 250$), el tiempo de la lista escala linealmente a $\\sim 0.25\\text{ segundos}$ por consulta, lo que en horas pico saturará a los operadores. 

En cambio, la \*\*Tabla Hash\*\* crecerá a un factor constante $\\Theta(1 + \\alpha)$. Si dimensionamos la tabla con $m=2.500.000$ casillas, mantendremos $\\alpha = 2$, por lo que buscar entre 5 millones de envíos \*\*tardará exactamente los mismos escasos microsegundos que con 20.000 guías\*\*. ¡Es la solución definitiva!

