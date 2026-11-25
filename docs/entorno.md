# Entorno experimental

- Equipo: AMD Ryzen 5 PRO 2400G with Radeon Vega Graphics
- Sistema: Windows 10 · AMD64 · 8 núcleos lógicos
- Python: CPython 3.12.10
- Fecha de las series A/B/C: 2026-11-25
- Series 1 y 2: aplicaciones y perfil de energía no registrados.
- Serie 3: Integrante A/R1 confirmó conexión a corriente, perfil equilibrado y cierre de aplicaciones pesadas/sincronizadores antes de la corrida; esta confirmación es manual, no proviene de sensores.
- Sensores: `psutil` no instalado; frecuencia, temperatura, RSS y energía no disponibles.
- Datos: semilla fija 7; preparación fuera del cronómetro.
- Series: 10 repeticiones por combinación en cada CSV; la segunda se ejecutó por CV > 10 % y la tercera bajo condiciones controladas.
- Archivos de entorno completos: `resultados/resultados_A_B_C_serie1.entorno.json` y
  `resultados/resultados_A_B_C_serie2.entorno.json` y
  `resultados/resultados_A_B_C_serie3.entorno.json`.

Las mediciones de tiempo A/B/C se ejecutaron con el mismo equipo, versión de
Python, datos y protocolo. Las condiciones de control de la serie 3 se anotaron
en las filas del CSV; no se pueden verificar con sensores. No se combinan con
la evidencia histórica A/C realizada con CPython 3.14.7.
