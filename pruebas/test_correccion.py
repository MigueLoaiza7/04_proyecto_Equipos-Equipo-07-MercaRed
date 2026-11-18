"""
Pruebas de corrección (R2). Ejecutar:  python -m unittest discover -s pruebas
Una estrategia más rápida pero incorrecta NO es una mejora.
"""
import unittest

from experimentos.ejecutar_experimento import ESTRATEGIAS
from src import estrategia_c, linea_base


class TestCorreccion(unittest.TestCase):
    def test_preparar_es_reproducible(self):
        primero = linea_base.preparar(300)
        segundo = linea_base.preparar(300)

        self.assertEqual(primero, segundo)
        self.assertEqual(len(primero[0]), 300)
        self.assertEqual(len(primero[1]), 30)

    def test_ordenar_insercion_ordena_sin_modificar_entrada(self):
        catalogo = [(8, "Ocho", 8.0), (2, "Dos", 2.0), (5, "Cinco", 5.0)]
        original = list(catalogo)

        ordenado = linea_base.ordenar_insercion(catalogo)

        self.assertEqual([producto[0] for producto in ordenado], [2, 5, 8])
        self.assertEqual(catalogo, original)

    def test_buscar_lineal_encuentra_y_reporta_codigos_ausentes(self):
        catalogo = [(1, "Uno", 1.0), (3, "Tres", 3.0)]

        self.assertEqual(linea_base.buscar_lineal(catalogo, 3), catalogo[1])
        self.assertIsNone(linea_base.buscar_lineal(catalogo, 2))
        self.assertIsNone(linea_base.buscar_lineal([], 1))

    def test_ejecutar_cuenta_solo_consultas_encontradas(self):
        datos = (
            [(3, "Tres", 3.0), (1, "Uno", 1.0), (2, "Dos", 2.0)],
            [1, 3, 7, 2, 1],
        )
        original = (list(datos[0]), list(datos[1]))

        self.assertEqual(linea_base.ejecutar(datos), 4)
        self.assertEqual(datos, original)

    def test_estrategias_registradas_coinciden_con_linea_base(self):
        casos = [
            linea_base.preparar(300),
            ([(3, "Tres", 3.0), (1, "Uno", 1.0)], [1, 3, 7, 1]),
            ([], [1, -1]),
        ]

        for nombre, estrategia in ESTRATEGIAS.items():
            for indice, datos in enumerate(casos):
                with self.subTest(estrategia=nombre, caso=indice):
                    esperado = linea_base.ejecutar(datos)
                    self.assertEqual(estrategia.ejecutar(datos), esperado)

    def test_estrategia_c_igual_a_base(self):
        casos = [
            linea_base.preparar(300),
            ([(3, "Tres", 3.0), (1, "Uno", 1.0)], [1, 3, 7, 1]),
            ([], [1, -1]),
        ]

        for indice, datos in enumerate(casos):
            with self.subTest(caso=indice):
                self.assertEqual(
                    estrategia_c.ejecutar(datos),
                    linea_base.ejecutar(datos),
                )

    def test_estrategia_c_no_modifica_catalogo(self):
        d = linea_base.preparar(300)
        datos_originales = (list(d[0]), list(d[1]))

        estrategia_c.ejecutar(d)

        self.assertEqual(d, datos_originales)

    def test_indice_directo_encuentra_codigo(self):
        catalogo = [(3, "Tres", 3.0), (1, "Uno", 1.0)]
        indice = estrategia_c.construir_indice(catalogo)

        self.assertEqual(estrategia_c.buscar_indirecto(indice, 3), catalogo[0])
        self.assertIsNone(estrategia_c.buscar_indirecto(indice, 7))
        self.assertEqual(estrategia_c.construir_indice([]), {})


if __name__ == "__main__":
    unittest.main()
