"""Resume el CSV del laboratorio y genera resumen, atipicos y figuras SVG."""

import argparse
import csv
import math
from collections import defaultdict
from pathlib import Path

T_CRITICO_95 = {
    1: 12.706, 2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571,
    6: 2.447, 7: 2.365, 8: 2.306, 9: 2.262, 10: 2.228,
    11: 2.201, 12: 2.179, 13: 2.160, 14: 2.145, 15: 2.131,
    16: 2.120, 17: 2.110, 18: 2.101, 19: 2.093, 20: 2.086,
    21: 2.080, 22: 2.074, 23: 2.069, 24: 2.064, 25: 2.060,
    26: 2.056, 27: 2.052, 28: 2.048, 29: 2.045, 30: 2.042,
}


def promedio(valores):
    return sum(valores) / len(valores)


def desviacion_muestral(valores, media):
    if len(valores) < 2:
        return 0.0
    return math.sqrt(sum((valor - media) ** 2 for valor in valores) / (len(valores) - 1))


def percentil(valores, fraccion):
    ordenados = sorted(valores)
    posicion = (len(ordenados) - 1) * fraccion
    inferior = math.floor(posicion)
    superior = math.ceil(posicion)
    if inferior == superior:
        return ordenados[inferior]
    return ordenados[inferior] + (ordenados[superior] - ordenados[inferior]) * (posicion - inferior)


def resumen_grupo(valores):
    media = promedio(valores)
    desviacion = desviacion_muestral(valores, media)
    cv = desviacion / media * 100 if media else 0.0
    grados_libertad = len(valores) - 1
    t = T_CRITICO_95.get(grados_libertad, 1.96 if grados_libertad > 30 else None)
    if t is None:
        raise ValueError(f"No hay valor t de Student registrado para n={len(valores)}")
    margen = t * desviacion / math.sqrt(len(valores))
    return {
        "n_repeticiones": len(valores),
        "media_s": media,
        "mediana_s": percentil(valores, 0.5),
        "desviacion_s": desviacion,
        "cv_pct": cv,
        "ic95_inf_s": max(0.0, media - margen),
        "ic95_sup_s": media + margen,
    }


def escribir_svg_tiempo(ruta, resumen, estrategias, tamanos):
    ancho, alto = 900, 560
    izquierda, derecha, arriba, abajo = 105, 45, 70, 90
    puntos = [
        fila for fila in resumen
        if fila["estrategia"] in estrategias and int(fila["n"]) in tamanos
    ]
    x_min, x_max = min(tamanos), max(tamanos)
    limites_positivos = [fila["ic95_inf_s"] for fila in puntos if fila["ic95_inf_s"] > 0]
    y_min = min(limites_positivos) * 0.75 if limites_positivos else min(fila["media_s"] for fila in puntos) * 0.1
    y_max = max(fila["ic95_sup_s"] for fila in puntos) * 1.3

    def x_coord(valor):
        if x_min == x_max:
            return (izquierda + ancho - derecha) / 2
        return izquierda + (math.log10(valor) - math.log10(x_min)) / (math.log10(x_max) - math.log10(x_min)) * (ancho - izquierda - derecha)

    def y_coord(valor):
        valor = max(valor, y_min)
        return alto - abajo - (math.log10(valor) - math.log10(y_min)) / (math.log10(y_max) - math.log10(y_min)) * (alto - arriba - abajo)

    colores = {"A_linea_base": "#2457a6", "C_indice_directo": "#d04a35"}
    lineas = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{ancho}" height="{alto}" viewBox="0 0 {ancho} {alto}">',
        '<rect width="100%" height="100%" fill="white"/>',
        '<text x="450" y="30" text-anchor="middle" font-family="sans-serif" font-size="19">Tiempo de pared vs. n (escala log-log)</text>',
        f'<path d="M {izquierda} {arriba} V {alto-abajo} H {ancho-derecha}" fill="none" stroke="#333"/>',
        f'<text x="500" y="{alto-25}" text-anchor="middle" font-family="sans-serif" font-size="15">Tamano n (productos), escala logaritmica</text>',
        f'<text x="25" y="300" transform="rotate(-90 25 300)" text-anchor="middle" font-family="sans-serif" font-size="15">Tiempo (s), media e IC 95%</text>',
    ]
    for tamano in tamanos:
        x = x_coord(tamano)
        lineas.extend([
            f'<path d="M {x:.2f} {arriba} V {alto-abajo}" stroke="#ddd"/>',
            f'<text x="{x:.2f}" y="{alto-abajo+25}" text-anchor="middle" font-family="sans-serif" font-size="12">{tamano}</text>',
        ])
    for estrategia in estrategias:
        grupo = sorted((fila for fila in puntos if fila["estrategia"] == estrategia), key=lambda fila: int(fila["n"]))
        coords = []
        for fila in grupo:
            x = x_coord(int(fila["n"]))
            y = y_coord(fila["media_s"])
            y_inf = y_coord(fila["ic95_inf_s"])
            y_sup = y_coord(fila["ic95_sup_s"])
            color = colores.get(estrategia, "#444")
            coords.append(f"{x:.2f},{y:.2f}")
            lineas.extend([
                f'<path d="M {x:.2f} {y_sup:.2f} V {y_inf:.2f} M {x-5:.2f} {y_sup:.2f} H {x+5:.2f} M {x-5:.2f} {y_inf:.2f} H {x+5:.2f}" stroke="{color}" stroke-width="2"/>',
                f'<circle cx="{x:.2f}" cy="{y:.2f}" r="4" fill="{color}"/>',
            ])
        lineas.append(f'<polyline points="{" ".join(coords)}" fill="none" stroke="{colores.get(estrategia, "#444")}" stroke-width="2"/>')
    for indice, estrategia in enumerate(estrategias):
        x = izquierda + indice * 220
        color = colores.get(estrategia, "#444")
        lineas.extend([
            f'<path d="M {x} 55 H {x+25}" stroke="{color}" stroke-width="3"/>',
            f'<text x="{x+32}" y="60" font-family="sans-serif" font-size="13">{estrategia}</text>',
        ])
    lineas.append("</svg>")
    ruta.write_text("\n".join(lineas), encoding="utf-8")


def escribir_svg_comparacion(ruta, resumen, estrategias, tamano):
    ancho, alto = 760, 500
    izquierda, derecha, arriba, abajo = 105, 55, 75, 100
    grupo = [fila for fila in resumen if fila["estrategia"] in estrategias and int(fila["n"]) == tamano]
    limites_positivos = [fila["ic95_inf_s"] for fila in grupo if fila["ic95_inf_s"] > 0]
    minimo = min(limites_positivos) * 0.65 if limites_positivos else min(fila["media_s"] for fila in grupo) * 0.1
    maximo = max(fila["ic95_sup_s"] for fila in grupo) * 1.4
    rango_y = alto - arriba - abajo

    def y_coord(valor):
        valor = max(valor, minimo)
        return alto - abajo - (math.log10(valor) - math.log10(minimo)) / (math.log10(maximo) - math.log10(minimo)) * rango_y

    lineas = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{ancho}" height="{alto}" viewBox="0 0 {ancho} {alto}">',
        '<rect width="100%" height="100%" fill="white"/>',
        f'<text x="{ancho/2}" y="32" text-anchor="middle" font-family="sans-serif" font-size="18">Comparacion en n={tamano}: media e IC 95% (escala log)</text>',
        f'<path d="M {izquierda} {arriba} V {alto-abajo} H {ancho-derecha}" fill="none" stroke="#333"/>',
        f'<text x="{ancho/2}" y="{alto-32}" text-anchor="middle" font-family="sans-serif" font-size="14">Estrategia</text>',
        f'<text x="25" y="280" transform="rotate(-90 25 280)" text-anchor="middle" font-family="sans-serif" font-size="14">Tiempo medio (s), escala logaritmica</text>',
    ]
    centros = [250, 520]
    colores = {"A_linea_base": "#2457a6", "C_indice_directo": "#d04a35"}
    for indice, estrategia in enumerate(estrategias):
        fila = next(fila for fila in grupo if fila["estrategia"] == estrategia)
        x = centros[indice]
        media_y = y_coord(fila["media_s"])
        low_y = y_coord(fila["ic95_inf_s"])
        high_y = y_coord(fila["ic95_sup_s"])
        color = colores.get(estrategia, "#444")
        lineas.extend([
            f'<path d="M {x} {high_y:.2f} V {low_y:.2f} M {x-8} {high_y:.2f} H {x+8} M {x-8} {low_y:.2f} H {x+8}" stroke="{color}" stroke-width="3"/>',
            f'<circle cx="{x}" cy="{media_y:.2f}" r="7" fill="{color}"/>',
            f'<text x="{x}" y="{alto-abajo+28}" text-anchor="middle" font-family="sans-serif" font-size="14">{estrategia}</text>',
            f'<text x="{x}" y="{media_y-14:.2f}" text-anchor="middle" font-family="sans-serif" font-size="12">{fila["media_s"]:.6g} s</text>',
        ])
    lineas.append("</svg>")
    ruta.write_text("\n".join(lineas), encoding="utf-8")


def analizar(entrada, directorio):
    with entrada.open(newline="", encoding="utf-8-sig") as archivo:
        lector = csv.DictReader(archivo)
        campos = lector.fieldnames or []
        filas = list(lector)
    requeridos = {"estrategia", "n", "repeticion", "tiempo_s", "pico_mem_mib", "medicion_memoria"}
    faltantes = requeridos - set(campos)
    if faltantes:
        raise ValueError(f"Faltan columnas requeridas: {', '.join(sorted(faltantes))}")

    tiempos = defaultdict(list)
    memorias = {}
    conteo_vacios = {campo: sum(not fila.get(campo, "").strip() for fila in filas) for campo in campos}
    for fila in filas:
        clave = (fila["estrategia"], int(fila["n"]))
        if fila["medicion_memoria"].strip().lower() == "si":
            memorias[clave] = float(fila["pico_mem_mib"])
        elif fila["medicion_memoria"].strip().lower() == "no":
            tiempos[clave].append((int(fila["repeticion"]), float(fila["tiempo_s"])))
        else:
            raise ValueError(f"Valor medicion_memoria desconocido en fila: {fila}")

    directorio.mkdir(parents=True, exist_ok=True)
    resumen = []
    atipicos = []
    for clave in sorted(tiempos, key=lambda par: (par[0], par[1])):
        estrategia, tamano = clave
        datos = tiempos[clave]
        valores = [tiempo for _, tiempo in datos]
        estadistica = resumen_grupo(valores)
        iqr = percentil(valores, 0.75) - percentil(valores, 0.25)
        limite_inferior = percentil(valores, 0.25) - 1.5 * iqr
        limite_superior = percentil(valores, 0.75) + 1.5 * iqr
        fila_resumen = {
            "estrategia": estrategia,
            "n": tamano,
            **estadistica,
            "memoria_pico_mib": memorias.get(clave, ""),
            "atipicos_tukey": sum(valor < limite_inferior or valor > limite_superior for valor in valores),
        }
        resumen.append(fila_resumen)
        for repeticion, valor in datos:
            if valor < limite_inferior or valor > limite_superior:
                atipicos.append({
                    "estrategia": estrategia,
                    "n": tamano,
                    "repeticion": repeticion,
                    "tiempo_s": valor,
                    "cv_pct": estadistica["cv_pct"],
                    "limite_tukey_inf_s": limite_inferior,
                    "limite_tukey_sup_s": limite_superior,
                })

    resumen_path = directorio / "resumen.csv"
    with resumen_path.open("w", newline="", encoding="utf-8") as archivo:
        columnas = list(resumen[0])
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()
        escritor.writerows(resumen)
    atipicos_path = directorio / "atipicos.csv"
    with atipicos_path.open("w", newline="", encoding="utf-8") as archivo:
        columnas = ["estrategia", "n", "repeticion", "tiempo_s", "cv_pct", "limite_tukey_inf_s", "limite_tukey_sup_s"]
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()
        escritor.writerows(atipicos)
    auditoria_path = directorio / "auditoria_datos.csv"
    with auditoria_path.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["columna", "celdas_vacias", "filas"])
        escritor.writeheader()
        escritor.writerows(
            {"columna": campo, "celdas_vacias": conteo_vacios[campo], "filas": len(filas)}
            for campo in campos
        )

    estrategias = sorted({fila["estrategia"] for fila in resumen})
    tamanos = sorted({int(fila["n"]) for fila in resumen})
    escribir_svg_tiempo(directorio / "tiempo_vs_n.svg", resumen, estrategias, tamanos)
    escribir_svg_comparacion(directorio / "comparacion_n_mayor.svg", resumen, estrategias, max(tamanos))
    return {
        "rows": filas,
        "columns": campos,
        "empty_counts": conteo_vacios,
        "timing_count": sum(len(values) for values in tiempos.values()),
        "memory_count": len(memorias),
        "summary": resumen,
        "outliers": atipicos,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", nargs="?", default="resultados/resultados.csv")
    parser.add_argument("--salida", default="resultados")
    argumentos = parser.parse_args()
    resultado = analizar(Path(argumentos.csv), Path(argumentos.salida))
    print(f"Filas: {len(resultado['rows'])} (tiempo={resultado['timing_count']}, memoria={resultado['memory_count']})")
    print(f"Columnas: {', '.join(resultado['columns'])}")
    print(f"Atipicos Tukey: {len(resultado['outliers'])}")
    for fila in resultado["summary"]:
        print(
            f"{fila['estrategia']} n={fila['n']}: media={fila['media_s']:.9f} s, "
            f"IC95%=[{fila['ic95_inf_s']:.9f}, {fila['ic95_sup_s']:.9f}], "
            f"CV={fila['cv_pct']:.2f}%, memoria={fila['memoria_pico_mib']} MiB, "
            f"atipicos={fila['atipicos_tukey']}"
        )
    print(f"Resultados de analisis en: {argumentos.salida}")


if __name__ == "__main__":
    main()
