"""Script para calcular el promedio de una lista de números."""

def calcular_promedio(lista_numeros: list[int]) -> float:
    """Calcula el promedio matemático de una lista de números.

    Args:
        lista_numeros: Lista con los números enteros a promediar.

    Returns:
        El promedio calculado como un valor flotante (decimal).
    """
    suma_total = 0
    for numero in lista_numeros:
        suma_total += numero

    return suma_total / len(lista_numeros)


def main() -> None:
    """Punto de entrada principal del script."""
    numeros = [1, 2, 3, 4, 5]
    resultado = calcular_promedio(numeros)
    print(resultado)


if __name__ == "__main__":
    main()