"""Experimento comparativo entre Insertion Sort y Merge Sort."""

import os
import time
import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio


def ejecutar() -> None:
    tamanos = [100, 200, 400, 800, 1600, 3200, 6400]
    tiempos_insertion = []
    tiempos_merge = []

    for n in tamanos:
        lote = generar_aleatorio(n)

        # Medición Insertion Sort
        t0 = time.perf_counter()
        insertion_sort(lote)
        t1 = time.perf_counter()
        tiempos_insertion.append(t1 - t0)

        # Medición Merge Sort
        t0 = time.perf_counter()
        merge_sort(lote)
        t1 = time.perf_counter()
        tiempos_merge.append(t1 - t0)

    os.makedirs("graficas", exist_ok=True)

    plt.figure(figsize=(8, 5))
    plt.plot(tamanos, tiempos_insertion, label="Insertion Sort", marker="o", color="red")
    plt.plot(tamanos, tiempos_merge, label="Merge Sort", marker="s", color="blue")
    plt.title("Tiempo de Ejecución: Insertion Sort vs. Merge Sort (Escenario A)")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("graficas/parte4_tiempo.png")
    plt.close()


if __name__ == "__main__":
    ejecutar()