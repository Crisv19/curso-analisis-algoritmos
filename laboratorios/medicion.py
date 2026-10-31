"""Script para medir y graficar los tiempos de busqueda."""
import time
import random
import matplotlib.pyplot as plt
from estructuras import ListaEnlazada, TablaHash

def generar_guias_inexistentes(existentes: set[int], cantidad: int, semilla: int = 7) -> list[int]:
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes

def experimento_a():
    print("Iniciando Experimento A (Lista vs Tabla)... esto tomará unos segundos.")
    tamanos_n = [100, 500, 1000, 5000, 10000, 20000]
    primos_m = [53, 251, 503, 2503, 5003, 10007] # Para mantener alfa cercano a 2
    tiempos_lista = []
    tiempos_tabla = []

    random.seed(42)
    for i, n in enumerate(tamanos_n):
        lista = ListaEnlazada()
        tabla = TablaHash(primos_m[i])
        existentes = set()

        # Insertar datos
        for _ in range(n):
            guia = random.randint(10**9, 10**10 - 1)
            existentes.add(guia)
            lista.insertar(guia, "estado")
            tabla.insertar(guia, "estado")

        inexistentes = generar_guias_inexistentes(existentes, 200)

        # Medir Lista
        inicio = time.perf_counter()
        for guia in inexistentes:
            lista.buscar(guia)
        tiempos_lista.append((time.perf_counter() - inicio) / 200)

        # Medir Tabla
        inicio = time.perf_counter()
        for guia in inexistentes:
            tabla.buscar(guia)
        tiempos_tabla.append((time.perf_counter() - inicio) / 200)
        print(f"  -> Tamaño {n} procesado.")

    # Generar gráfica A
    plt.figure(figsize=(10, 6))
    plt.plot(tamanos_n, tiempos_lista, label='Lista Enlazada Θ(n)', marker='o', color='red')
    plt.plot(tamanos_n, tiempos_tabla, label='Tabla Hash Θ(1+α)', marker='s', color='blue')
    plt.title("Tiempo medio de búsqueda infructuosa vs Número de Guías (n)")
    plt.xlabel("Número de guías (n)")
    plt.ylabel("Tiempo medio por búsqueda (segundos)")
    plt.legend()
    plt.grid(True)
    plt.savefig('graficas/lista_vs_tabla.png')
    print("Gráfica A guardada.")

def experimento_b():
    print("\nIniciando Experimento B (Efecto del factor de carga Alfa)...")
    n = 20000
    alfas = [0.5, 1, 4, 10]
    primos_m = [39989, 19997, 5003, 1999] # Casillas para generar esos alfas
    tiempos_tabla = []

    random.seed(42)
    existentes = set()
    guias = [random.randint(10**9, 10**10 - 1) for _ in range(n)]
    existentes.update(guias)
    inexistentes = generar_guias_inexistentes(existentes, 200)

    for i, m in enumerate(primos_m):
        tabla = TablaHash(m)
        for guia in guias:
            tabla.insertar(guia, "estado")

        inicio = time.perf_counter()
        for guia in inexistentes:
            tabla.buscar(guia)
        tiempos_tabla.append((time.perf_counter() - inicio) / 200)
        print(f"  -> Tabla con alfa {alfas[i]} procesada.")

    # Generar gráfica B
    plt.figure(figsize=(10, 6))
    plt.plot(alfas, tiempos_tabla, label='Tabla Hash', marker='s', color='green')
    plt.title("Tiempo medio de búsqueda vs Factor de Carga (α)")
    plt.xlabel("Factor de carga (α = n/m)")
    plt.ylabel("Tiempo medio por búsqueda (segundos)")
    plt.legend()
    plt.grid(True)
    plt.savefig('graficas/tiempo_vs_alfa.png')
    print("Gráfica B guardada.\n¡Ambos experimentos completados exitosamente!")

if __name__ == "__main__":
    experimento_a()
    experimento_b()