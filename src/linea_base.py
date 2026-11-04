"""
Línea base — Equipo 7: Algoritmos de búsqueda y ordenamiento.

Situación inicial: el catálogo de la tienda en línea se ORDENA por código con
un ordenamiento por inserción escrito a mano y, para atender las consultas,
cada código se BUSCA recorriendo la lista de principio a fin.

preparar(n) -> (catalogo de n productos desordenados, lista de consultas)
ejecutar(datos) -> número de consultas encontradas

El número de consultas es n // 10 (las consultas crecen con el catálogo).
"""
import random
import time


def preparar(n: int, semilla: int = 7):
    rng = random.Random(semilla)
    codigos = rng.sample(range(10 * n), n)
    catalogo = [(c, f"Producto {c}", round(rng.uniform(1_000, 900_000), 2)) for c in codigos]
    consultas = [rng.choice(codigos) if rng.random() < .8 else -1 for _ in range(max(1, n // 10))]
    return catalogo, consultas


def ordenar_insercion(lista):
    a = list(lista)
    for i in range(1, len(a)):
        actual, j = a[i], i - 1
        while j >= 0 and a[j][0] > actual[0]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = actual
    return a


def buscar_lineal(ordenado, codigo):
    for p in ordenado:
        if p[0] == codigo:
            return p
    return None


def ejecutar(datos) -> int:
    catalogo, consultas = datos
    ordenado = ordenar_insercion(catalogo)
    return sum(buscar_lineal(ordenado, c) is not None for c in consultas)


if __name__ == "__main__":
    for n in (1_000, 2_000, 4_000):
        d = preparar(n)
        t0 = time.perf_counter()
        r = ejecutar(d)
        print(f"n = {n:>5}: {r} encontradas en {time.perf_counter() - t0:.3f} s")
