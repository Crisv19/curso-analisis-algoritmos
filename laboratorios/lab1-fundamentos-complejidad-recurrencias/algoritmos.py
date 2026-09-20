"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de índices de riesgo de mayor a menor riesgo.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de índices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el número total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    arreglo = datos.copy()
    comparaciones = 0

    for i in range(1, len(arreglo)):
        clave = arreglo[i]
        j = i - 1

        while j >= 0:
            comparaciones += 1
            if arreglo[j] < clave:  # Para orden descendente (mayor a menor)
                arreglo[j + 1] = arreglo[j]
                j -= 1
            else:
                break

        arreglo[j + 1] = clave

    return arreglo, comparaciones


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de índices de riesgo mediante divide y vencerás.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de índices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada de mayor a menor y el número
        total de comparaciones entre elementos realizadas en la mezcla.
    """
    arreglo = datos.copy()

    if len(arreglo) <= 1:
        return arreglo, 0

    mitad = len(arreglo) // 2
    izq, comp_izq = merge_sort(arreglo[:mitad])
    der, comp_der = merge_sort(arreglo[mitad:])

    resultado, comp_merge = _merge(izq, der)

    return resultado, comp_izq + comp_der + comp_merge


def _merge(izquierda: list[int], derecha: list[int]) -> tuple[list[int], int]:
    """Combina dos listas ya ordenadas de mayor a menor."""
    resultado: list[int] = []
    i = j = 0
    comparaciones = 0

    while i < len(izquierda) and j < len(derecha):
        comparaciones += 1
        if izquierda[i] >= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado, comparaciones