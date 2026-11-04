"""
Pruebas de corrección (R2). Ejecutar:  python -m unittest discover -s pruebas
Una estrategia más rápida pero incorrecta NO es una mejora.
"""
import unittest

from src import linea_base


class TestCorreccion(unittest.TestCase):
    def test_linea_base_ejecuta(self):
        d = linea_base.preparar(300)
        self.assertIsNotNone(linea_base.ejecutar(d))

    # TODO (R2): una prueba por estrategia que compare su resultado con la línea base
    # def test_estrategia_b_igual_a_base(self):
    #     d = linea_base.preparar(300)
    #     self.assertEqual(estrategia_b.ejecutar(d), linea_base.ejecutar(d))


if __name__ == "__main__":
    unittest.main()
