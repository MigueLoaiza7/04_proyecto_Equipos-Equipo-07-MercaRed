# Entorno experimental

- Equipo: AMD Ryzen 5 PRO 2400G with Radeon Vega Graphics
- Sistema: Windows 10 · AMD64 · 8 núcleos lógicos
- Python: CPython 3.12.10
- Fecha de las series A/B/C: 2026-11-25
- Aplicaciones y perfil de energía: no registrados durante estas corridas.
- Sensores: `psutil` no instalado; frecuencia, temperatura, RSS y energía no disponibles.
- Datos: semilla fija 7; preparación fuera del cronómetro.
- Series: 10 repeticiones por combinación en cada CSV; segunda serie ejecutada por CV > 10 %.
- Archivos de entorno completos: `resultados/resultados_A_B_C_serie1.entorno.json` y
  `resultados/resultados_A_B_C_serie2.entorno.json`.

Las mediciones de tiempo A/B/C se ejecutaron con el mismo equipo, versión de
Python, datos y protocolo. No se combinan con la evidencia histórica A/C
realizada con CPython 3.14.7.
