"""
Pruebas de corrección (R2). Ejecutar:  python -m unittest discover -s pruebas
Una estrategia más rápida pero incorrecta NO es una mejora.
"""
import unittest

from src import estrategia_c, linea_base


class TestCorreccion(unittest.TestCase):
    def test_linea_base_ejecuta(self):
        d = linea_base.preparar(300)
        self.assertIsNotNone(linea_base.ejecutar(d))

    def test_estrategia_c_igual_a_base(self):
        d = linea_base.preparar(300)
        self.assertEqual(estrategia_c.ejecutar(d), linea_base.ejecutar(d))

    def test_estrategia_c_no_modifica_catalogo(self):
        d = linea_base.preparar(300)
        catalogo_original = list(d[0])
        estrategia_c.ejecutar(d)
        self.assertEqual(d[0], catalogo_original)

    def test_indice_directo_encuentra_codigo(self):
        d = linea_base.preparar(300)
        indice = estrategia_c.construir_indice(d[0])
        for codigo in d[1]:
            encontrado = estrategia_c.buscar_indirecto(indice, codigo)
            if encontrado is not None:
                self.assertEqual(encontrado[0], codigo)


if __name__ == "__main__":
    unittest.main()
