"""Clasificador de años bisiestos.
 
Complete las funciones siguiendo la especificación de cada docstring.
"""


def es_bisiesto(anio: int) -> bool:
    """Determina si un año es bisiesto.
 
    Un año es bisiesto si es divisible por 4, excepto los años
    divisibles por 100 que no lo sean también por 400.
 
    Args:
        anio: año a evaluar (número entero).
 
    Returns:
        True si el año es bisiesto, False en caso contrario.
    """
    if anio % 400 == 0:
        return True
    elif anio % 100 == 0:
        return False
    elif anio % 4 == 0:
        return True
    else:
        return False


def leer_anios() -> list[int]:
    """Solicita al usuario una lista de años separados por comas.
 
    Debe reintentar mientras la entrada no se pueda convertir a enteros
    (use try / except para capturar entradas inválidas).
 
    Returns:
        Lista de años como enteros.
    """
    while True:
        entrada = input("Ingrese años separados por comas (ej. 2000,2023,2024): ")
        try:
            # Convierte cada elemento separado por comas a un entero
            lista_anios = [int(anio.strip()) for anio in entrada.split(",")]
            return lista_anios
        except ValueError:
            print("Error: Ingrese únicamente números enteros separados por comas.\n")


def main() -> None:
    """Punto de entrada del script."""
    anios_ingresados = leer_anios()

    # Comprensión de listas para filtrar solo los años bisiestos
    anios_bisiestos = [anio for anio in anios_ingresados if es_bisiesto(anio)]

    print(f"\nAños ingresados: {anios_ingresados}")
    print(f"Años bisiestos: {anios_bisiestos}")
    print(f"Cantidad de años bisiestos: {len(anios_bisiestos)} de {len(anios_ingresados)}")


if __name__ == "__main__":
    main()