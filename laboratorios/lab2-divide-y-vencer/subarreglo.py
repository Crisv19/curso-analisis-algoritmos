"""Subarreglo maximo: fuerza bruta y divide y venceras."""

def subarreglo_fuerza_bruta(valores: list[float]) -> tuple[int, int, float]:
    """Encuentra la mejor racha probando todos los pares de dias (i, j).

    Args:
        valores: variacion diaria de caja, una por dia. Tiene al menos
            un elemento.

    Returns:
        Una tupla (inicio, fin, suma) con los indices inclusivos del
        tramo de mayor suma y el valor de esa suma.
    """
    mejor_inicio: int = 0
    mejor_fin: int = 0
    suma_maxima: float = float('-inf')

    for i in range(len(valores)):
        suma_actual: float = 0.0
        for j in range(i, len(valores)):
            suma_actual += valores[j]
            if suma_actual > suma_maxima:
                suma_maxima = suma_actual
                mejor_inicio = i
                mejor_fin = j

    return mejor_inicio, mejor_fin, suma_maxima


def suma_cruzada(
    valores: list[float], inicio: int, medio: int, fin: int
) -> tuple[int, int, float]:
    """Encuentra el mejor tramo que cruza el punto medio.

    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango considerado (inclusive).
        medio: indice del ultimo elemento de la mitad izquierda.
        fin: indice final del rango considerado (inclusive).

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo que incluye al
        menos un elemento de cada mitad.
    """
    suma_max_izq: float = float('-inf')
    suma_actual: float = 0.0
    mejor_izq: int = medio
    for i in range(medio, inicio - 1, -1):
        suma_actual += valores[i]
        if suma_actual > suma_max_izq:
            suma_max_izq = suma_actual
            mejor_izq = i

    suma_max_der: float = float('-inf')
    suma_actual = 0.0
    mejor_der: int = medio + 1
    for j in range(medio + 1, fin + 1):
        suma_actual += valores[j]
        if suma_actual > suma_max_der:
            suma_max_der = suma_actual
            mejor_der = j

    return mejor_izq, mejor_der, suma_max_izq + suma_max_der


def subarreglo_maximo(
    valores: list[float], inicio: int, fin: int
) -> tuple[int, int, float]:
    """Encuentra la mejor racha por divide y venceras.

    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango a considerar (inclusive).
        fin: indice final del rango a considerar (inclusive).

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo dentro de
        valores[inicio..fin].
    """
    if inicio == fin:
        return inicio, fin, float(valores[inicio])

    medio: int = (inicio + fin) // 2

    i_izq, f_izq, suma_izq = subarreglo_maximo(valores, inicio, medio)
    i_der, f_der, suma_der = subarreglo_maximo(valores, medio + 1, fin)
    i_cruz, f_cruz, suma_cruz = suma_cruzada(valores, inicio, medio, fin)

    if suma_izq >= suma_der and suma_izq >= suma_cruz:
        return i_izq, f_izq, suma_izq
    if suma_der >= suma_izq and suma_der >= suma_cruz:
        return i_der, f_der, suma_der
    return i_cruz, f_cruz, suma_cruz