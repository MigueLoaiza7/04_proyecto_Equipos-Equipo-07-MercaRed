"""
Pruebas de corrección (R2). Ejecutar:  python -m unittest discover -s pruebas
Una estrategia más rápida pero incorrecta NO es una mejora.
"""
import unittest

from src import estrategia_a, linea_base


class TestCorreccion(unittest.TestCase):
    def test_linea_base_ejecuta(self):
        d = linea_base.preparar(300)
        self.assertIsNotNone(linea_base.ejecutar(d))

    def test_estrategia_a_igual_a_base(self):
        d = linea_base.preparar(300)
        self.assertEqual(estrategia_a.ejecutar(d), linea_base.ejecutar(d))

    def test_estrategia_a_no_modifica_catalogo(self):
        d = linea_base.preparar(300)
        catalogo_original = list(d[0])
        estrategia_a.ejecutar(d)
        self.assertEqual(d[0], catalogo_original)


if __name__ == "__main__":
    unittest.main()
