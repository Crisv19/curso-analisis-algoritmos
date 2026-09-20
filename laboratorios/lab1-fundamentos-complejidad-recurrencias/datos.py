"""Generadores de lotes de registros para los escenarios de Tamiza."""

import random


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (Escenario A)."""
    random.seed(semilla)
    return random.sample(range(1, 1_000_000 + n * 10), n)


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (Escenario B)."""
    base = generar_aleatorio(n, semilla)
    n_ordenados = int(n * 0.98)

    # 98% de la lista ordenado de mayor a menor
    parte_ordenada = sorted(base[:n_ordenados], reverse=True)
    parte_desordenada = base[n_ordenados:]

    return parte_ordenada + parte_desordenada


def generar_inverso(n: int) -> list[int]:
    """Genera un lote en orden ascendente (peor caso para mayor a menor) (Escenario C)."""
    base = generar_aleatorio(n, semilla=42)
    return sorted(base)