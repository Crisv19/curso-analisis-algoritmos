"""Experimento de evaluación de Insertion Sort en los escenarios de Tamiza."""

import os
import time
import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso


def ejecutar() -> None:
    tamanos = [100, 200, 400, 800, 1600, 3200, 6400]
    tiempos = {"A": [], "B": [], "C": []}
    comparaciones = {"A": [], "B": [], "C": []}

    for n in tamanos:
        lotes = {
            "A": generar_aleatorio(n),
            "B": generar_casi_ordenado(n),
            "C": generar_inverso(n),
        }

        for esc in ["A", "B", "C"]:
            t0 = time.perf_counter()
            _, comp = insertion_sort(lotes[esc])
            t1 = time.perf_counter()

            tiempos[esc].append(t1 - t0)
            comparaciones[esc].append(comp)

    os.makedirs("graficas", exist_ok=True)

    # Gráfica 1: Comparaciones
    plt.figure(figsize=(8, 5))
    plt.plot(tamanos, comparaciones["A"], label="Escenario A (Aleatorio)", marker="o")
    plt.plot(tamanos, comparaciones["B"], label="Escenario B (Casi Ordenado)", marker="s")
    plt.plot(tamanos, comparaciones["C"], label="Escenario C (Inverso)", marker="^")
    plt.title("Insertion Sort: Comparaciones vs. Tamaño de Entrada")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Número de comparaciones")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("graficas/parte3_comparaciones.png")
    plt.close()

    # Gráfica 2: Tiempo
    plt.figure(figsize=(8, 5))
    plt.plot(tamanos, tiempos["A"], label="Escenario A (Aleatorio)", marker="o")
    plt.plot(tamanos, tiempos["B"], label="Escenario B (Casi Ordenado)", marker="s")
    plt.plot(tamanos, tiempos["C"], label="Escenario C (Inverso)", marker="^")
    plt.title("Insertion Sort: Tiempo vs. Tamaño de Entrada")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("graficas/parte3_tiempo.png")
    plt.close()


if __name__ == "__main__":
    ejecutar()