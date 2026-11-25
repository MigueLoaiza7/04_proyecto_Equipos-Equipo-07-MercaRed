"""Resume CSV de mediciones y genera los dos gráficos exigidos por el informe.

Uso:
    python -m experimentos.analizar_resultados resultados/resultados_A_B_C.csv
    python -m experimentos.analizar_resultados serie_1.csv serie_2.csv

Si se proporcionan varias series, se reportan por separado y también agrupadas.
Los gráficos representan el conjunto agrupado cuando hay varias entradas.
"""
import argparse
import csv
import math
import statistics
from collections import defaultdict
from pathlib import Path

try:
    import matplotlib.pyplot as plt
except ImportError as exc:
    raise SystemExit(
        "Para generar los gráficos instala la dependencia declarada: "
        "python -m pip install matplotlib"
    ) from exc


ESTRATEGIAS = ("A_linea_base", "B_mezcla_busqueda_binaria", "C_indice_directo")
ETIQUETAS = {
    "A_linea_base": "A · Inserción + búsqueda lineal",
    "B_mezcla_busqueda_binaria": "B · Mezcla + búsqueda binaria",
    "C_indice_directo": "C · Índice directo",
}
ETIQUETAS_CORTAS = {
    "A_linea_base": "A\nInserción + lineal",
    "B_mezcla_busqueda_binaria": "B\nMezcla + binaria",
    "C_indice_directo": "C\nÍndice directo",
}
T_CRITICO_95 = {
    4: 2.776,
    5: 2.571,
    6: 2.447,
    7: 2.365,
    8: 2.306,
    9: 2.262,
    10: 2.228,
    11: 2.201,
    12: 2.179,
    13: 2.160,
    14: 2.145,
    15: 2.131,
    16: 2.120,
    17: 2.110,
    18: 2.101,
    19: 2.093,
    20: 2.086,
    21: 2.080,
    22: 2.074,
    23: 2.069,
    24: 2.064,
    25: 2.060,
    26: 2.056,
    27: 2.052,
    28: 2.048,
    29: 2.045,
}


def cargar_mediciones(rutas):
    tiempos = defaultdict(list)
    memoria = {}
    series = []

    for ruta in rutas:
        with ruta.open(encoding="utf-8", newline="") as archivo:
            lector = csv.DictReader(archivo)
            requeridos = {"estrategia", "n", "repeticion", "tiempo_s", "medicion_memoria"}
            faltantes = requeridos.difference(lector.fieldnames or ())
            if faltantes:
                raise ValueError(f"{ruta}: faltan columnas requeridas: {sorted(faltantes)}")

            etiqueta = ruta.stem
            series.append(etiqueta)
            for fila in lector:
                estrategia = fila["estrategia"]
                if estrategia not in ESTRATEGIAS:
                    raise ValueError(f"{ruta}: estrategia desconocida: {estrategia}")
                n = int(fila["n"])
                if fila["medicion_memoria"] == "si":
                    if fila["pico_mem_mib"]:
                        memoria[(etiqueta, estrategia, n)] = float(fila["pico_mem_mib"])
                else:
                    tiempos[(etiqueta, estrategia, n)].append(float(fila["tiempo_s"]))

    return series, tiempos, memoria


def resumir(muestras, pico_memoria=None):
    cantidad = len(muestras)
    if cantidad < 5:
        raise ValueError(f"Se requieren al menos 5 repeticiones; se encontraron {cantidad}")
    media = statistics.mean(muestras)
    desviacion = statistics.stdev(muestras)
    grados_libertad = cantidad - 1
    t_critico = T_CRITICO_95.get(grados_libertad, 1.96 if grados_libertad >= 30 else None)
    if t_critico is None:
        raise ValueError("El intervalo t requiere al menos 5 repeticiones")
    semiancho = t_critico * desviacion / math.sqrt(cantidad)
    return {
        "repeticiones": cantidad,
        "media_s": media,
        "desviacion_estandar_s": desviacion,
        "cv_pct": desviacion / media * 100 if media else 0.0,
        "ic95_inferior_s": media - semiancho,
        "ic95_superior_s": media + semiancho,
        "pico_memoria_mib": "" if pico_memoria is None else pico_memoria,
    }


def calcular_pendiente_loglog(puntos):
    if len(puntos) < 2:
        return ""
    log_n = [math.log(n) for n, _ in puntos]
    log_t = [math.log(tiempo) for _, tiempo in puntos]
    media_log_n = statistics.mean(log_n)
    media_log_t = statistics.mean(log_t)
    varianza_log_n = sum((x - media_log_n) ** 2 for x in log_n)
    covarianza = sum(
        (x - media_log_n) * (y - media_log_t)
        for x, y in zip(log_n, log_t)
    )
    return covarianza / varianza_log_n


def escribir_resumen(ruta, registros):
    campos = [
        "serie",
        "estrategia",
        "n",
        "repeticiones",
        "media_s",
        "desviacion_estandar_s",
        "cv_pct",
        "ic95_inferior_s",
        "ic95_superior_s",
        "pico_memoria_mib",
        "pendiente_loglog",
    ]
    with ruta.open("w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for registro in registros:
            escritor.writerow(registro)


def graficar(salida, resumen, estrategias):
    tamanos = sorted({registro["n"] for registro in resumen})
    colores = {
        "A_linea_base": "#1f77b4",
        "B_mezcla_busqueda_binaria": "#ff7f0e",
        "C_indice_directo": "#2ca02c",
    }

    fig, eje = plt.subplots(figsize=(8, 5))
    for estrategia in estrategias:
        registros = sorted(
            (r for r in resumen if r["estrategia"] == estrategia),
            key=lambda r: r["n"],
        )
        if not registros:
            continue
        medias = [r["media_s"] for r in registros]
        inferiores = [r["media_s"] - r["ic95_inferior_s"] for r in registros]
        superiores = [r["ic95_superior_s"] - r["media_s"] for r in registros]
        eje.errorbar(
            [r["n"] for r in registros],
            medias,
            yerr=[inferiores, superiores],
            marker="o",
            capsize=4,
            label=ETIQUETAS[estrategia],
            color=colores[estrategia],
        )
    eje.set_xscale("log")
    eje.set_yscale("log")
    eje.set_xlabel("Tamaño del catálogo, n (productos)")
    eje.set_ylabel("Tiempo de ejecución (s)")
    eje.set_title("Tiempo de ejecución vs. tamaño del catálogo (IC95 %)")
    eje.grid(True, which="both", linestyle=":", alpha=0.6)
    eje.legend()
    fig.tight_layout()
    fig.savefig(salida / "grafico_tiempo_loglog.png", dpi=160)
    plt.close(fig)

    n_mayor = max(tamanos)
    registros = [r for r in resumen if r["n"] == n_mayor]
    registros.sort(key=lambda r: estrategias.index(r["estrategia"]))
    fig, eje = plt.subplots(figsize=(8, 5))
    medias = [r["media_s"] for r in registros]
    inferiores = [r["media_s"] - r["ic95_inferior_s"] for r in registros]
    superiores = [r["ic95_superior_s"] - r["media_s"] for r in registros]
    eje.errorbar(
        [ETIQUETAS_CORTAS[r["estrategia"]] for r in registros],
        medias,
        yerr=[inferiores, superiores],
        fmt="o",
        capsize=5,
        color="#4c4c4c",
    )
    eje.set_yscale("log")
    eje.set_ylabel("Tiempo de ejecución (s)")
    eje.tick_params(axis="x", labelsize=9)
    eje.set_title(f"Comparación de estrategias para n = {n_mayor:,} (IC95 %)")
    eje.grid(True, axis="y", which="both", linestyle=":", alpha=0.6)
    fig.tight_layout()
    fig.savefig(salida / "grafico_estrategias_n_mayor.png", dpi=160)
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "entradas",
        nargs="+",
        type=Path,
        help="Uno o más CSV de mediciones; cada archivo se trata como una serie",
    )
    parser.add_argument("--salida-dir", type=Path, default=Path("resultados"))
    args = parser.parse_args()

    series, tiempos, memoria = cargar_mediciones(args.entradas)
    if not tiempos:
        raise ValueError("No hay mediciones de tiempo en los CSV")

    args.salida_dir.mkdir(parents=True, exist_ok=True)
    resumen = []
    for (serie, estrategia, n), muestras in sorted(tiempos.items()):
        registro = {
            "serie": serie,
            "estrategia": estrategia,
            "n": n,
            **resumir(muestras, memoria.get((serie, estrategia, n))),
        }
        resumen.append(registro)

    etiqueta_combinada = "series_combinadas" if len(series) > 1 else series[0]
    combinadas = defaultdict(list)
    memorias_combinadas = defaultdict(list)
    for (serie, estrategia, n), muestras in tiempos.items():
        combinadas[(estrategia, n)].extend(muestras)
        pico = memoria.get((serie, estrategia, n))
        if pico is not None:
            memorias_combinadas[(estrategia, n)].append(pico)

    resumen_grafico = []
    for (estrategia, n), muestras in sorted(combinadas.items()):
        picos = memorias_combinadas[(estrategia, n)]
        registro = {
            "serie": etiqueta_combinada,
            "estrategia": estrategia,
            "n": n,
            **resumir(muestras, statistics.mean(picos) if picos else None),
        }
        resumen.append(registro)
        resumen_grafico.append(registro)

    puntos_por_serie_y_estrategia = defaultdict(list)
    for registro in resumen:
        puntos_por_serie_y_estrategia[
            (registro["serie"], registro["estrategia"])
        ].append((registro["n"], registro["media_s"]))

    pendientes = {}
    for clave, puntos in puntos_por_serie_y_estrategia.items():
        puntos.sort()
        pendientes[clave] = calcular_pendiente_loglog(puntos)

    for registro in resumen:
        registro["pendiente_loglog"] = pendientes[
            (registro["serie"], registro["estrategia"])
        ]

    escribir_resumen(args.salida_dir / "resumen_estadistico_A_B_C.csv", resumen)
    graficar(args.salida_dir, resumen_grafico, ESTRATEGIAS)
    print(f"Resumen: {args.salida_dir / 'resumen_estadistico_A_B_C.csv'}")
    print(f"Gráfico log-log: {args.salida_dir / 'grafico_tiempo_loglog.png'}")
    print(f"Gráfico n mayor: {args.salida_dir / 'grafico_estrategias_n_mayor.png'}")


if __name__ == "__main__":
    main()
