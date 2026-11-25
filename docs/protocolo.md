# Protocolo experimental reproducible

**Responsables:** Integrante A (R1/R4) · **Revisado por:** Integrantes B y C · **Versión:** 1 · **Fecha:**

## 1. Objetivo del experimento

Comparar A (ordenamiento por inserción y búsqueda lineal), B (ordenamiento por
mezcla y búsqueda binaria) y C (índice directo) mediante tiempo de pared, CPU,
memoria Python y RSS disponible.

## 2. Preparación del entorno (antes de cada sesión)
1. **Integrante A (R1/R4)** prepara el equipo conectado a corriente, selecciona
   el perfil de energía equilibrado y cierra navegador, editores pesados y
   sincronizadores de archivos.
2. A registra fecha/hora, perfil, aplicaciones abiertas y cualquier incidente
   en `docs/entorno.md`; envía esa confirmación a **Integrante C (R3/R4)** antes
   de la corrida. No completar estos datos por suposición.
3. C verifica que los tamaños, semillas y versión de código sigan el protocolo,
   usa una ruta CSV nueva y conserva el CSV y el JSON de entorno.
4. Generar datos con semilla fija: `python -m src.generar_datos <n>`.

## 3. Procedimiento
| Paso | Acción | Comando | Evidencia |
|---|---|---|---|
| 1 | Pruebas de corrección | `python -m unittest discover -s pruebas` | captura |
| 2 | Prueba de humo | `python -m experimentos.ejecutar_experimento --rapido` | CSV |
| 3 | Primera serie formal | `python -m experimentos.ejecutar_experimento --salida resultados/resultados_A_B_C_serie1.csv` | CSV y entorno JSON |
| 4 | Serie adicional si CV > 10 % | `python -m experimentos.ejecutar_experimento --salida resultados/resultados_A_B_C_serie2.csv --observacion "serie adicional CV"` | CSV y entorno JSON separados |
| 5 | Serie controlada tras CV alto | `python -m experimentos.ejecutar_experimento --salida resultados/resultados_A_B_C_serie3.csv --observacion "serie controlada"` | CSV y entorno JSON separados |
| 6 | Análisis y gráficos | `python -m experimentos.analizar_resultados resultados/resultados_A_B_C_serie1.csv resultados/resultados_A_B_C_serie2.csv resultados/resultados_A_B_C_serie3.csv` | CSV resumen y dos PNG |
| 7 | (Opcional) monitoreo | `python herramientas/... monitor_sistema.py` en otra terminal | `resultados/monitor.csv` |

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
  permanece sobre el umbral tras repetir en condiciones controladas, declarar
  los resultados exploratorios y describir las limitaciones; no añadir series
  sin registrar qué condición se busca controlar.
- Valores atípicos (regla de Tukey): se reportan; solo se excluyen con causa documentada.

## 6. Registro de incidentes
| Fecha/hora | Incidente (p. ej. actualización del SO, batería) | Corridas afectadas | Decisión |
|---|---|---|---|

Integrante A registra los incidentes y condiciones físicas; Integrante C integra
ese registro con las mediciones, estadísticas y figuras en su rama. B (R2/R3)
verifica la corrección antes de abrir o actualizar un PR.
