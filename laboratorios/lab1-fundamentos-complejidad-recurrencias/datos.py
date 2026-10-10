import random

def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """
    Genera una lista de tamaño n con números aleatorios sin repetición.
    
    Args:
        n (int): Tamaño de la lista a generar.
        semilla (int, opcional): Semilla para reproducibilidad. Por defecto 42.
        
    Returns:
        list[int]: Lista con enteros desordenados.
    """
    random.seed(semilla)
    return random.sample(range(1, n * 10), n)

def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """
    Genera una lista de tamaño n casi ordenada de mayor a menor (98%).
   
    
    Args:
        n (int): Tamaño de la lista a generar.
        semilla (int, opcional): Semilla para reproducibilidad. Por defecto 42.
        
    Returns:
        list[int]: Lista de enteros con aproximadamente el 2% de desorden.
    """
    random.seed(semilla)
    # Generamos la lista ya ordenada de forma descendente matemáticamente
    lista: list[int] = list(range(n, 0, -1))
    
    # Intercambiamos aleatoriamente posiciones para desordenar el 2%
    num_desordenar: int = max(1, int(n * 0.02))
    for _ in range(num_desordenar):
        i: int = random.randint(0, n - 1)
        j: int = random.randint(0, n - 1)
        lista[i], lista[j] = lista[j], lista[i]
        
    return lista

def generar_inverso(n: int) -> list[int]:
    """
    Genera una lista de tamaño n en orden estricto de menor a mayor (peor caso).
    
    Args:
        n (int): Tamaño de la lista a generar.
        
    Returns:
        list[int]: Lista de enteros en orden ascendente.
    """
    # Generamos la lista ascendente matemáticamente
    return list(range(1, n + 1))