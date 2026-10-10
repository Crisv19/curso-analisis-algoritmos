"""Script de verificacion para los algoritmos del subarreglo maximo."""
import random
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

def ejecutar_pruebas():
    # 1. Caso base (problema de la gerente)
    serie_gerente = [-3, 5, -2, 8, -6, 3, 9, -4]
    assert subarreglo_fuerza_bruta(serie_gerente)[2] == 17
    assert subarreglo_maximo(serie_gerente, 0, len(serie_gerente) - 1)[2] == 17

    # 2. Serie de un solo elemento
    serie_unica = [42]
    assert subarreglo_fuerza_bruta(serie_unica)[2] == 42
    assert subarreglo_maximo(serie_unica, 0, 0)[2] == 42

    # 3. Todos negativos
    serie_negativos = [-5, -2, -9, -1]
    assert subarreglo_fuerza_bruta(serie_negativos)[2] == -1
    assert subarreglo_maximo(serie_negativos, 0, 3)[2] == -1

    # 4. Todos positivos
    serie_positivos = [1, 2, 3, 4]
    assert subarreglo_fuerza_bruta(serie_positivos)[2] == 10
    assert subarreglo_maximo(serie_positivos, 0, 3)[2] == 10

    # 5. Caso cruzado evidente (maximo en el centro exacto)
    serie_cruzada = [-10, 5, 5, -10]
    assert subarreglo_fuerza_bruta(serie_cruzada)[2] == 10
    assert subarreglo_maximo(serie_cruzada, 0, 3)[2] == 10

    # 6. Al menos 20 listas aleatorias
    random.seed(42)
    for _ in range(20):
        n = random.randint(10, 100)
        arreglo_aleatorio = [random.randint(-100, 100) for _ in range(n)]
        
        suma_fb = subarreglo_fuerza_bruta(arreglo_aleatorio)[2]
        suma_dv = subarreglo_maximo(arreglo_aleatorio, 0, n - 1)[2]
        assert suma_fb == suma_dv, f"Fallo en {arreglo_aleatorio}"

    print("¡Todas las pruebas pasaron exitosamente!")

if __name__ == "__main__":
    ejecutar_pruebas()