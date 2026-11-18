# Protocolo experimental reproducible

**Responsable:** R1 · **Revisado por:** todos · **Versión:** 1 · **Fecha:**

## 1. Objetivo del experimento

Comparar la línea base A con la Estrategia C de índice directo mediante
tiempo de pared, CPU, memoria Python y RSS disponible.

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
| 3 | Experimento formal | `python -m experimentos.ejecutar_experimento` | `resultados/resultados.csv` |
| 4 | (Opcional) monitoreo | `python herramientas/... monitor_sistema.py` en otra terminal | `resultados/monitor.csv` |

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
  documentada. Realizar una serie adicional de al menos 10 repeticiones bajo
  condiciones estables y reportar tanto la serie original como la adicional;
  no sustituir resultados silenciosamente.
- Valores atípicos (regla de Tukey): se reportan; solo se excluyen con causa documentada.

## 6. Registro de incidentes
| Fecha/hora | Incidente (p. ej. actualización del SO, batería) | Corridas afectadas | Decisión |
|---|---|---|---|
