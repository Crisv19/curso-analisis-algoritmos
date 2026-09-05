\# Laboratorio 02 - Configuración del entorno de trabajo



\## Creación y activación del entorno virtual

Para crear y activar el entorno virtual aislado desde la raíz del repositorio se utilizaron los siguientes comandos en Windows:

1\. Creación: `python -m venv venv`

2\. Activación: `venv\\Scripts\\activate`



Se verificó la presencia del prefijo `(venv)` en la terminal antes de realizar cualquier instalación.



\## Reproducibilidad del entorno

Para reproducir exactamente este entorno de trabajo en otro equipo:

1\. Clonar el repositorio y ubicar la terminal en la raíz.

2\. Crear y activar un nuevo entorno virtual.

3\. Ejecutar: `pip install -r requirements.txt`

