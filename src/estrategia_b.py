"""
Estrategia B: ordenamiento por mezcla y búsqueda binaria.

Ordena una copia del catálogo por código y aprovecha ese orden para resolver
cada consulta sin recorrer toda la lista.
"""


def ordenar_mezcla(catalogo):
    """Devuelve una copia ordenada por código usando mezcla iterativa."""
    ordenado = list(catalogo)
    auxiliar = ordenado.copy()
    ancho = 1

    while ancho < len(ordenado):
        for inicio in range(0, len(ordenado), 2 * ancho):
            medio = min(inicio + ancho, len(ordenado))
            fin = min(inicio + 2 * ancho, len(ordenado))
            izquierda = inicio
            derecha = medio
            destino = inicio

            while izquierda < medio and derecha < fin:
                if ordenado[izquierda][0] <= ordenado[derecha][0]:
                    auxiliar[destino] = ordenado[izquierda]
                    izquierda += 1
                else:
                    auxiliar[destino] = ordenado[derecha]
                    derecha += 1
                destino += 1

            while izquierda < medio:
                auxiliar[destino] = ordenado[izquierda]
                izquierda += 1
                destino += 1

            while derecha < fin:
                auxiliar[destino] = ordenado[derecha]
                derecha += 1
                destino += 1

        ordenado, auxiliar = auxiliar, ordenado
        ancho *= 2

    return ordenado


def buscar_binaria(ordenado, codigo):
    """Devuelve el producto con el código indicado o None si no existe."""
    izquierda = 0
    derecha = len(ordenado)

    while izquierda < derecha:
        medio = (izquierda + derecha) // 2
        codigo_medio = ordenado[medio][0]
        if codigo_medio < codigo:
            izquierda = medio + 1
        else:
            derecha = medio

    if izquierda < len(ordenado) and ordenado[izquierda][0] == codigo:
        return ordenado[izquierda]
    return None


def ejecutar(datos) -> int:
    catalogo, consultas = datos
    ordenado = ordenar_mezcla(catalogo)
    return sum(buscar_binaria(ordenado, codigo) is not None for codigo in consultas)
