# Entorno experimental

## Medición histórica A/C — 18-11-2026

- Equipo: Equipo 7
- Fecha de medición: 2026-11-18
- Sistema y Python: Windows 10, CPython 3.14.7, AMD64
- Procesador informado: AMD64 Family 23 Model 17 Stepping 0, AuthenticAMD
- Núcleos lógicos: 8
- Aplicaciones y alimentación: no registradas en el JSON del experimento; no
  se puede reconstruir cuáles programas estaban abiertos ni el perfil de
  energía usado
- Conexión a corriente y lectura de corriente: no registradas
- Temperatura, frecuencia y energía RAPL: no disponibles
- RSS: no medido; `psutil` no estaba instalado
- El JSON completo es `resultados/resultados.entorno.json`.
- Antes de una eventual sesión aprobada, registrar fecha/hora, conexión a
  corriente (y lectura/unidad/instrumento si está disponible), perfil de
  energía y programas abiertos según [protocolo.md](protocolo.md). No inferir
  esos valores para la sesión anterior.
- No se localizaron en el repositorio ni en el entorno local los scripts
  `03_Clase_5/Scripts/analizar_resultados.py` y `verificar_hipotesis.py`;
  el análisis se reprodujo con el script local basado en la biblioteca estándar.

## Serie 3 controlada A/B/C — 25-11-2026

- Fecha/hora registrada: 2026-11-25 10:45:27.370; la zona horaria no está
  especificada en el JSON.
- Equipo: AMD Ryzen 5 PRO 2400G with Radeon Vega Graphics; Windows 10,
  AMD64, 8 núcleos lógicos; CPython 3.12.10.
- Corriente: equipo conectado, según confirmación manual de A/R1; no se
  registró una lectura de corriente eléctrica.
- Perfil de energía: equilibrado, según confirmación manual.
- Aplicaciones: la observación de las corridas informa que se cerraron
  procesos pesados; la confirmación general menciona aplicaciones pesadas y
  sincronizadores. No se anotaron nombres individuales, así que no se afirma
  cuáles programas concretos se cerraron.
- Incidentes: no hay un incidente específico en el CSV ni en el JSON de esta
  serie. Se reporta como “sin incidentes registrados”; no permite asegurar
  que no ocurriera alguno.
- Frecuencia, temperatura, RSS y energía no estuvieron disponibles; la
  confirmación de corriente y perfil fue manual, no sensorizada.

Esta es una serie separada de la medición histórica A/C del 18-11-2026; no se
combinan sus datos porque se usaron versiones distintas de Python. El CSV y el
JSON fuente están en el
[registro de la serie 3](https://github.com/MigueLoaiza7/04_proyecto_Equipos-Equipo-07-MercaRed/blob/c411d194ea61e3b59b8b67bba8572556e2109b21/resultados/resultados_A_B_C_serie3.csv)
y su [metadato de entorno](https://github.com/MigueLoaiza7/04_proyecto_Equipos-Equipo-07-MercaRed/blob/c411d194ea61e3b59b8b67bba8572556e2109b21/resultados/resultados_A_B_C_serie3.entorno.json).
