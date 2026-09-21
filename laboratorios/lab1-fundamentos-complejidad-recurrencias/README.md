 Laboratorio Evaluativo 01 — Fundamentos, Complejidad y Recurrencias



Cristian Jose Mendez Guzman

Septiembre 2026  






\## Instrucciones de Reproducción



Para ejecutar los experimentos y regenerar las gráficas desde la carpeta del laboratorio (`laboratorios/lab1-fundamentos-complejidad-recurrencias/`):



1\. \*\*Activar el entorno virtual\*\* desde la raíz del repositorio:

&#x20;  ```cmd

&#x20;  ..\\..\\venv\\Scripts\\activate
+


 Analizar el algoritmo antes de comprar hardware

Insertion Sort es correcto pero inviable: ordena bien la lista, pero falla en procesar los 1.200.000 datos dentro de la ventana estricta de 4 horas (2:00 a.m. a 6:00 a.m.).

Comprar un servidor el doble de rápido no arregla el problema. Como es un algoritmo cuadrático $O(n^2)$, al pasar de 20.000 a 1.200.000 datos (60 veces más), las operaciones aumentan $60^2 = 3.600$ veces. Reducir el tiempo a la mitad con mejor hardware no sirve de nada frente a ese crecimiento.


Responsabilidad ambiental y ética

Ambiental: Con un algoritmo optimizado de 15 minutos, el consumo cae, reduciendo la huella de carbono.
Ética: Que el proceso no termine a tiempo causa dos problemas:
  1. Pacientes críticos no llamados: El costo de salud lo pagan el paciente y su familia.
  2. Operadores llamando sin prioridad: El costo operativo lo asume la Secretaría de Salud.

Concepto Técnico para la Secretaría de Salud

Recomendación: Cambiar a Merge Sort. No podemos confiar en recibir datos ordenados en producción.
 Extrapolación (1.2M registros):Insertion Sort toma ~4,8 horas. Merge Sort toma solo ~1,5 segundos.Dictamen de Hardware, Rechazar la compra del servidor, duplicar el procesador solo reduce Insertion Sort* a 2,4 horas; cambiar el código resuelve el problema gratis.


