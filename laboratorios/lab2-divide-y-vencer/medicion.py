"""Script para medir y graficar los tiempos de ejecucion."""
import time
import random
import matplotlib.pyplot as plt
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

def ejecutar_experimento():
    # Tamaños de entrada (n) desde muy pequeños hasta 4000
    tamanos = [10, 50, 100, 500, 1000, 2000, 4000]
    tiempos_fb = []
    tiempos_dv = []

    # Semilla fija para que el profe pueda reproducir los mismos datos
    random.seed(42)

    print("Iniciando experimento... Esto tomará unos segundos.")

    for n in tamanos:
        # Generar datos de prueba para el tamaño n
        valores = [random.randint(-100, 100) for _ in range(n)]

        # Medir Fuerza Bruta
        inicio_fb = time.perf_counter()
        _, _, suma_fb = subarreglo_fuerza_bruta(valores)
        fin_fb = time.perf_counter()
        tiempos_fb.append(fin_fb - inicio_fb)

        # Medir Divide y Vencerás
        inicio_dv = time.perf_counter()
        _, _, suma_dv = subarreglo_maximo(valores, 0, n - 1)
        fin_dv = time.perf_counter()
        tiempos_dv.append(fin_dv - inicio_dv)

        # Verificación interna de correctitud
        assert suma_fb == suma_dv, f"Resultados no coinciden en tamaño {n}"
        print(f"Tamaño {n} procesado.")

    # Generar gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(tamanos, tiempos_fb, label='Fuerza Bruta Θ(n²)', marker='o', color='red')
    plt.plot(tamanos, tiempos_dv, label='Divide y Vencerás Θ(n log n)', marker='s', color='blue')
    
    plt.title("Tiempo de Ejecución: Subarreglo Máximo")
    plt.xlabel("Tamaño de entrada (n) [Cantidad de días]")
    plt.ylabel("Tiempo de ejecución [segundos]")
    plt.legend()
    plt.grid(True)
    
    # Guardar en la carpeta graficas
    plt.savefig('graficas/tiempo_vs_n.png')
    print("¡Experimento completado! Gráfica guardada en 'graficas/tiempo_vs_n.png'.")

if __name__ == "__main__":
    ejecutar_experimento()