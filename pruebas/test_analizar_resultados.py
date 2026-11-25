import csv
import tempfile
import unittest
from pathlib import Path

from experimentos.analizar_resultados import analizar, resumen_grupo


class TestAnalizarResultados(unittest.TestCase):
    def test_resumen_usa_intervalo_t_y_cv(self):
        resultado = resumen_grupo([1.0, 1.0, 1.0])
        self.assertEqual(resultado["cv_pct"], 0)
        self.assertEqual(resultado["ic95_inf_s"], 1.0)
        self.assertEqual(resultado["ic95_sup_s"], 1.0)

    def test_analiza_corrida_rapida_de_un_solo_tamano(self):
        campos = ["estrategia", "n", "repeticion", "tiempo_s", "pico_mem_mib", "medicion_memoria"]
        with tempfile.TemporaryDirectory() as temporal:
            entrada = Path(temporal) / "entrada.csv"
            salida = Path(temporal) / "resultados"
            filas = []
            for estrategia, valores, memoria in (
                ("A", ["0.10", "0.12"], "0.010"),
                ("C", ["0.01", "0.012"], "0.050"),
            ):
                filas.extend(
                    {
                        "estrategia": estrategia,
                        "n": "1000",
                        "repeticion": str(indice),
                        "tiempo_s": valor,
                        "pico_mem_mib": "",
                        "medicion_memoria": "no",
                    }
                    for indice, valor in enumerate(valores, 1)
                )
                filas.append({
                    "estrategia": estrategia,
                    "n": "1000",
                    "repeticion": "0",
                    "tiempo_s": "0.5",
                    "pico_mem_mib": memoria,
                    "medicion_memoria": "si",
                })
            with entrada.open("w", newline="", encoding="utf-8") as archivo:
                escritor = csv.DictWriter(archivo, fieldnames=campos)
                escritor.writeheader()
                escritor.writerows(filas)

            resultado = analizar(entrada, salida)

            self.assertEqual(resultado["timing_count"], 4)
            self.assertEqual(resultado["memory_count"], 2)
            self.assertTrue((salida / "tiempo_vs_n.svg").exists())
            self.assertTrue((salida / "comparacion_n_mayor.svg").exists())
            self.assertTrue((salida / "auditoria_datos.csv").exists())
            self.assertTrue((salida / "resumen_a.csv").exists())
            self.assertTrue((salida / "atipicos_c.csv").exists())
            self.assertTrue((salida / "tiempo_c_vs_n.svg").exists())

            solo_c = Path(temporal) / "solo_c"
            analizar(entrada, solo_c, estrategia_foco="C")
            self.assertTrue((solo_c / "resumen_c.csv").exists())
            self.assertFalse((solo_c / "resumen_a.csv").exists())


if __name__ == "__main__":
    unittest.main()
