"""Script de verificacion para la lista enlazada y la tabla hash."""
import random
from estructuras import ListaEnlazada, TablaHash

def ejecutar_pruebas():
    # 1. Busquedas basicas
    lista = ListaEnlazada()
    lista.insertar(1000000010, "en bodega")
    assert lista.buscar(1000000010) == "en bodega"
    assert lista.buscar(9999999999) is None

    # 2. Colision forzada
    tabla = TablaHash(7)
    for guia in (10, 24, 17):
        tabla.insertar(guia, "en bodega")
    
    assert tabla.buscar(24) == "en bodega"
    assert tabla.buscar(10) == "en bodega"
    assert tabla.buscar(17) == "en bodega"
    assert tabla.buscar(99) is None
    assert tabla.factor_carga() == 3 / 7
    assert tabla.casillas[3].tamano == 3  # Validar tamano de la lista encadenada en la casilla 3

    # 3. Pruebas aleatorias comparativas
    random.seed(42)
    for _ in range(20):
        n = random.randint(50, 100)
        l_test = ListaEnlazada()
        t_test = TablaHash(23)
        guias_insertadas = []

        for _ in range(n):
            guia = random.randint(10**9, 10**10 - 1)
            estado = "estado_test"
            l_test.insertar(guia, estado)
            t_test.insertar(guia, estado)
            guias_insertadas.append(guia)

        # Buscar guia existente
        guia_buscar = random.choice(guias_insertadas)
        assert l_test.buscar(guia_buscar) == t_test.buscar(guia_buscar)

        # Buscar guia inexistente
        assert l_test.buscar(1) == t_test.buscar(1)

    print("¡Todas las pruebas pasaron exitosamente!")

if __name__ == "__main__":
    ejecutar_pruebas()