"""
Estrategia A: linea base del catalogo de MercaRed Colombia.

Ordena el catalogo mediante insercion y atiende cada consulta recorriendo
secuencialmente el catalogo ordenado.
"""

from src.linea_base import buscar_lineal, ordenar_insercion, preparar


def ejecutar(datos) -> int:
    catalogo, consultas = datos
    ordenado = ordenar_insercion(catalogo)
    return sum(buscar_lineal(ordenado, codigo) is not None for codigo in consultas)
