# Protocolo experimental reproducible

**Responsable:** R1 · **Revisado por:** todos · **Versión:** 1 · **Fecha:**

## 1. Objetivo del experimento

Comparar A (ordenamiento por inserción y búsqueda lineal), B (ordenamiento por
mezcla y búsqueda binaria) y C (índice directo) mediante tiempo de pared, CPU,
memoria Python y RSS disponible.

## 2. Preparación del entorno (antes de cada sesión)
1. Equipo conectado a corriente; perfil de energía "equilibrado" (anotar).
2. Cerrar navegador, editores pesados y sincronizadores de archivos.
3. Ejecutar `diagnostico_entorno.py` y guardar la salida en `docs/entorno.md`.
4. Generar datos con semilla fija: `python -m src.generar_datos <n>`.

## 3. Procedimiento
| Paso | Acción | Comando | Evidencia |
|---|---|---|---|
| 1 | Pruebas de corrección | `python -m unittest discover -s pruebas` | captura |
| 2 | Prueba de humo | `python -m experimentos.ejecutar_experimento --rapido` | CSV |
| 3 | Primera serie formal | `python -m experimentos.ejecutar_experimento --salida resultados/resultados_A_B_C_serie1.csv` | CSV y entorno JSON |
| 4 | Serie adicional si CV > 10 % | `python -m experimentos.ejecutar_experimento --salida resultados/resultados_A_B_C_serie2.csv --observacion "serie adicional CV"` | CSV y entorno JSON separados |
| 5 | Análisis y gráficos | `python -m experimentos.analizar_resultados resultados/resultados_A_B_C_serie1.csv resultados/resultados_A_B_C_serie2.csv` | CSV resumen y dos PNG |
| 6 | (Opcional) monitoreo | `python herramientas/... monitor_sistema.py` en otra terminal | `resultados/monitor.csv` |

## 4. Parámetros
- Tamaños n: 1 000, 2 000 y 4 000. Justificación: rango ejecutable y comparable en el laboratorio.
- Repeticiones por combinación: 10 de tiempo; prueba rápida usa 2.
- Calentamiento: una ejecución no registrada por módulo y tamaño.
- Orden: plan barajado con random.Random(42).
- Datos: semilla fija 7.
- Preparación fuera del cronómetro; memoria con trazado separado.

## 5. Criterios de calidad de los datos
- CV ≤ 10 % por combinación. Si se supera, revisar las condiciones de medición
  y el registro de incidentes, sin excluir datos salvo que exista una causa
  documentada. Ejecutar una serie adicional de 10 repeticiones en un CSV
  separado con `--observacion "serie adicional CV"`, y reportar ambas series
  y el resumen combinado; no sustituir resultados silenciosamente. Si el CV
  permanece sobre el umbral, declarar los resultados exploratorios y repetir
  en una sesión mejor controlada.
- Valores atípicos (regla de Tukey): se reportan; solo se excluyen con causa documentada.

## 6. Registro de incidentes
| Fecha/hora | Incidente (p. ej. actualización del SO, batería) | Corridas afectadas | Decisión |
|---|---|---|---|
