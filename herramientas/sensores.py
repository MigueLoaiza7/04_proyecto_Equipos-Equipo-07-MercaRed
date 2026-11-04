"""
sensores.py — Lectura OPCIONAL de magnitudes físicas del sistema.

Física Aplicada al Desarrollo de Software · SENA ADSO · Clase 4

Qué hace
--------
Intenta leer, sin permisos de administrador:
  * Frecuencia actual del procesador (MHz)        -> psutil o /proc/cpuinfo
  * Temperatura del paquete/CPU (°C)              -> psutil o /sys/class/thermal
  * Contador de energía RAPL de Intel (µJ -> J)   -> /sys/class/powercap (solo Linux + Intel)

Principio de diseño: NINGUNA función lanza excepción si el sensor no existe.
Si una magnitud no está disponible se devuelve None, y el laboratorio
continúa con las magnitudes que sí se pueden medir (tiempo, memoria, CPU %).

Advertencias físicas importantes
--------------------------------
* El porcentaje de CPU NO es potencia eléctrica. Es la fracción de tiempo
  que el proceso ocupó núcleos lógicos durante un intervalo.
* La temperatura reportada por el sensor es la de un punto del chip, con
  inercia térmica: cambia segundos después de que cambia la carga.
* RAPL es un MODELO interno del procesador calibrado por el fabricante,
  no un vatímetro externo. Mide el paquete del procesador (y a veces DRAM),
  no el computador completo. En muchos Linux recientes energy_uj solo se
  puede leer como root (mitigación de seguridad CVE-2020-8694); en ese
  caso se reporta como no disponible.

Uso rápido:
    python sensores.py
"""
from __future__ import annotations

import glob
import os
import platform
import time
from pathlib import Path

try:  # dependencia opcional
    import psutil  # type: ignore
except ImportError:  # pragma: no cover - depende del entorno
    psutil = None


# ---------------------------------------------------------------- frecuencia
def frecuencia_mhz() -> float | None:
    """Frecuencia actual promedio de los núcleos en MHz, o None."""
    if psutil is not None:
        try:
            f = psutil.cpu_freq()
            if f and f.current:
                return round(float(f.current), 1)
        except (OSError, NotImplementedError, AttributeError):
            pass
    cpuinfo = Path("/proc/cpuinfo")
    if cpuinfo.exists():
        valores = [
            float(linea.split(":")[1])
            for linea in cpuinfo.read_text(errors="ignore").splitlines()
            if linea.lower().startswith("cpu mhz")
        ]
        if valores:
            return round(sum(valores) / len(valores), 1)
    return None


# --------------------------------------------------------------- temperatura
_ETIQUETAS_PREFERIDAS = ("package", "tctl", "tdie", "cpu", "core")


def temperatura_c() -> float | None:
    """Temperatura de CPU en °C (mejor esfuerzo), o None si no hay sensor."""
    if psutil is not None and hasattr(psutil, "sensors_temperatures"):
        try:
            grupos = psutil.sensors_temperatures() or {}
        except (OSError, AttributeError):
            grupos = {}
        candidatos = []
        for nombre, lecturas in grupos.items():
            for lectura in lecturas:
                etiqueta = f"{nombre} {lectura.label}".lower()
                prioridad = next(
                    (i for i, p in enumerate(_ETIQUETAS_PREFERIDAS) if p in etiqueta),
                    len(_ETIQUETAS_PREFERIDAS),
                )
                if lectura.current and 0 < lectura.current < 125:
                    candidatos.append((prioridad, lectura.current))
        if candidatos:
            return round(min(candidatos)[1], 1)

    # Respaldo Linux: zonas térmicas del kernel (miligrados Celsius)
    for zona in sorted(glob.glob("/sys/class/thermal/thermal_zone*")):
        try:
            tipo = Path(zona, "type").read_text().strip().lower()
            if any(p in tipo for p in ("x86_pkg", "cpu", "soc", "acpitz")):
                mili = int(Path(zona, "temp").read_text().strip())
                if 0 < mili < 125_000:
                    return round(mili / 1000, 1)
        except (OSError, ValueError):
            continue
    return None


# --------------------------------------------------------------- energía RAPL
_RAPL = Path("/sys/class/powercap/intel-rapl:0")


def energia_rapl_j() -> float | None:
    """Lectura acumulada del contador RAPL del paquete en julios, o None."""
    archivo = _RAPL / "energy_uj"
    try:
        return int(archivo.read_text().strip()) / 1_000_000
    except (OSError, ValueError, PermissionError):
        return None


def rango_rapl_j() -> float | None:
    """Valor máximo del contador antes de reiniciarse a cero (desbordamiento)."""
    try:
        return int((_RAPL / "max_energy_range_uj").read_text().strip()) / 1_000_000
    except (OSError, ValueError, PermissionError):
        return None


def delta_energia_j(inicio: float | None, fin: float | None) -> float | None:
    """Energía consumida entre dos lecturas RAPL, corrigiendo el desbordamiento."""
    if inicio is None or fin is None:
        return None
    delta = fin - inicio
    if delta < 0:
        rango = rango_rapl_j()
        if rango is None:
            return None
        delta += rango
    return delta


# ------------------------------------------------------------------- informe
def disponibilidad() -> dict[str, bool]:
    """Qué magnitudes físicas se pueden registrar en este equipo."""
    return {
        "frecuencia": frecuencia_mhz() is not None,
        "temperatura": temperatura_c() is not None,
        "energia_rapl": energia_rapl_j() is not None,
        "psutil": psutil is not None,
    }


def _demo() -> None:
    print(f"Sistema: {platform.system()} {platform.release()} · {platform.machine()}")
    print(f"Núcleos lógicos: {os.cpu_count()}")
    print(f"psutil instalado: {'sí' if psutil else 'no (opcional: pip install psutil)'}")
    f = frecuencia_mhz()
    t = temperatura_c()
    print(f"Frecuencia actual: {f} MHz" if f else "Frecuencia: no disponible")
    print(f"Temperatura CPU:  {t} °C" if t else "Temperatura: no disponible -> usar plan B (ver Guía de medición)")
    e0 = energia_rapl_j()
    if e0 is None:
        print("Energía RAPL: no disponible (normal sin Intel/Linux o sin permisos de root)")
    else:
        time.sleep(1.0)
        de = delta_energia_j(e0, energia_rapl_j())
        print(f"Energía RAPL del paquete en 1 s en reposo: {de:.3f} J  ->  potencia media ≈ {de:.2f} W")


if __name__ == "__main__":
    _demo()
