import unittest

from experimentos.analizar_resultados import calcular_pendiente_loglog, resumir


class TestAnalisisResultados(unittest.TestCase):
    def test_resumen_calcula_media_dispersion_y_intervalo(self):
        resumen = resumir([1.0, 2.0, 3.0, 4.0, 5.0], pico_memoria=0.25)

        self.assertEqual(resumen["repeticiones"], 5)
        self.assertEqual(resumen["media_s"], 3.0)
        self.assertAlmostEqual(resumen["desviacion_estandar_s"], 1.58113883)
        self.assertAlmostEqual(resumen["cv_pct"], 52.7046, places=3)
        self.assertLess(resumen["ic95_inferior_s"], 3.0)
        self.assertGreater(resumen["ic95_superior_s"], 3.0)
        self.assertEqual(resumen["pico_memoria_mib"], 0.25)

    def test_resumen_rechaza_menos_de_cinco_repeticiones(self):
        with self.assertRaisesRegex(ValueError, "al menos 5 repeticiones"):
            resumir([1.0, 2.0, 3.0, 4.0])

    def test_pendiente_loglog_recupera_crecimiento_lineal(self):
        pendiente = calcular_pendiente_loglog(
            [(1000, 0.001), (2000, 0.002), (4000, 0.004)]
        )

        self.assertAlmostEqual(pendiente, 1.0)


if __name__ == "__main__":
    unittest.main()
