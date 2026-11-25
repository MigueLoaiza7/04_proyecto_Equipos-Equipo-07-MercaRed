"""
Estrategia C: indice directo del catalogo de MercaRed Colombia.

Construye un diccionario que relaciona cada codigo con su producto. Las
consultas se resuelven mediante acceso directo por clave.
"""

def construir_indice(catalogo):
    return {producto[0]: producto for producto in catalogo}


def buscar_indirecto(indice, codigo):
    return indice.get(codigo)


def ejecutar(datos) -> int:
    catalogo, consultas = datos
    indice = construir_indice(catalogo)
    return sum(buscar_indirecto(indice, codigo) is not None for codigo in consultas)
