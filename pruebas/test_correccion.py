"""
Pruebas de corrección (R2). Ejecutar:  python -m unittest discover -s pruebas
Una estrategia más rápida pero incorrecta NO es una mejora.
"""
import tempfile
import unittest
from pathlib import Path

from experimentos.ejecutar_experimento import ESTRATEGIAS, validar_salida_disponible
from src import estrategia_b, estrategia_c, linea_base


class TestCorreccion(unittest.TestCase):
    def test_runner_preserva_archivos_de_salida_existentes(self):
        with tempfile.TemporaryDirectory() as directorio:
            salida = Path(directorio) / "resultados.csv"
            entorno = salida.with_suffix(".entorno.json")
            contenido = "evidencia existente"
            entorno.write_text(contenido, encoding="utf-8")

            with self.assertRaises(FileExistsError):
                validar_salida_disponible(salida)

            self.assertTrue(entorno.exists())
            self.assertEqual(entorno.read_text(encoding="utf-8"), contenido)

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

    def test_estrategia_b_ordena_catalogos_vacios_y_de_tamano_impar(self):
        casos = [
            [],
            [(4, "Cuatro", 4.0)],
            [(8, "Ocho", 8.0), (2, "Dos", 2.0), (5, "Cinco", 5.0)],
        ]

        for catalogo in casos:
            with self.subTest(catalogo=catalogo):
                original = list(catalogo)
                ordenado = estrategia_b.ordenar_mezcla(catalogo)

                self.assertEqual(
                    [producto[0] for producto in ordenado],
                    sorted(producto[0] for producto in catalogo),
                )
                self.assertEqual(catalogo, original)

    def test_estrategia_b_busca_ausentes_y_preserva_datos(self):
        datos = (
            [(8, "Ocho", 8.0), (2, "Dos", 2.0), (5, "Cinco", 5.0)],
            [2, 8, 7, 5],
        )
        originales = (list(datos[0]), list(datos[1]))
        ordenado = estrategia_b.ordenar_mezcla(datos[0])

        self.assertEqual(estrategia_b.ejecutar(datos), 3)
        self.assertIsNone(estrategia_b.buscar_binaria(ordenado, 7))
        self.assertEqual(datos, originales)

    def test_todas_las_estrategias_coinciden_con_linea_base(self):
        casos = [
            linea_base.preparar(301),
            ([(4, "Cuatro", 4.0), (2, "Dos", 2.0)], [2, 4, 8, 2]),
            ([], [1, -1]),
        ]

        for nombre, estrategia in ESTRATEGIAS.items():
            for indice, datos in enumerate(casos):
                with self.subTest(estrategia=nombre, caso=indice):
                    self.assertEqual(
                        estrategia.ejecutar(datos),
                        linea_base.ejecutar(datos),
                    )


if __name__ == "__main__":
    unittest.main()
