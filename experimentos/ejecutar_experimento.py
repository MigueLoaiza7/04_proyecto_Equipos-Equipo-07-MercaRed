"""
ejecutar_experimento.py — Experimento controlado del Equipo 7.

Responsable principal: R4 (automatización de mediciones). Revisado por: R1 (protocolo).

Completar los TODO. No modificar la estructura de registro: el CSV debe poder
analizarse con 03_Clase_5/Scripts/analizar_resultados.py

Uso (desde la raíz del repositorio):
    python -m experimentos.ejecutar_experimento --rapido      # prueba de humo
    python -m experimentos.ejecutar_experimento               # experimento formal
"""
import argparse
import random
from pathlib import Path

from herramientas.labmedicion import Experimento, calentar
from src import estrategia_b, estrategia_c, linea_base

ESTRATEGIAS = {
    "A_linea_base": linea_base,
    "B_mezcla_busqueda_binaria": estrategia_b,
    "C_indice_directo": estrategia_c,
}

# Los tamaños permiten observar crecimiento sin exceder el tiempo disponible.
# La justificación completa está en docs/protocolo.md.
TAMANOS = [1_000, 2_000, 4_000]
REPETICIONES = 10


def validar_salida_disponible(salida: Path) -> None:
    entorno = salida.with_suffix(".entorno.json")
    if salida.exists() or entorno.exists():
        raise FileExistsError(
            f"El archivo de resultados o su entorno ya existe; elige otra ruta: {salida}"
        )


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--rapido", action="store_true")
    p.add_argument("--salida", default="resultados/resultados_A_B_C.csv")
    p.add_argument(
        "--observacion",
        default="",
        help="Etiqueta para identificar una serie adicional sin sobrescribir evidencia",
    )
    a = p.parse_args()
    tamanos = TAMANOS[:1] if a.rapido else TAMANOS
    reps = 2 if a.rapido else REPETICIONES
    salida = Path(a.salida)
    validar_salida_disponible(salida)

    datos = {n: linea_base.preparar(n) for n in tamanos}           # preparación: NO se mide
    for n, d in datos.items():                                       # verificación de corrección
        esperado = linea_base.ejecutar(d)
        for nombre, mod in ESTRATEGIAS.items():
            resultado = mod.ejecutar(d)
            if resultado != esperado:
                raise RuntimeError(f"{nombre} da un resultado distinto para n={n}")

    plan = [(e, n, r) for e in ESTRATEGIAS for n in tamanos for r in range(1, reps + 1)]
    random.Random(42).shuffle(plan)                                  # orden aleatorio (control de deriva)
    for mod in ESTRATEGIAS.values():
        calentar(mod.ejecutar, datos[tamanos[0]], veces=1)

    with Experimento(salida, equipo="Equipo 7") as exp:
        for i, (e, n, r) in enumerate(plan, 1):
            exp.medir(
                ESTRATEGIAS[e].ejecutar,
                datos[n],
                estrategia=e,
                n=n,
                repeticion=r,
                observacion=a.observacion,
            )
            if r == 1:
                exp.medir(
                    ESTRATEGIAS[e].ejecutar,
                    datos[n],
                    estrategia=e,
                    n=n,
                    repeticion=0,
                    medir_memoria=True,
                    observacion="corrida de memoria separada"
                    + (f"; {a.observacion}" if a.observacion else ""),
                )
            print(f"\r{i}/{len(plan)}", end="", flush=True)
    print(f"\nListo: {salida}")


if __name__ == "__main__":
    main()
