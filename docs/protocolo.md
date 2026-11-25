# Protocolo experimental reproducible

**Responsable:** R1 · **Revisado por:** todos · **Versión:** 1 · **Fecha:**

## 1. Objetivo del experimento

Comparar la línea base A con la Estrategia C de índice directo mediante
tiempo de pared, CPU, memoria Python y RSS disponible.

## 2. Preparación del entorno (antes de cada sesión)
1. Registrar fecha y hora de inicio, y si el equipo está conectado a corriente.
   Si hay un instrumento para medir corriente, anotar lectura, unidad e
   instrumento; si no, marcarla como no disponible.
2. Registrar el perfil de energía realmente seleccionado y los programas
   abiertos al iniciar la medición. Después, cerrar navegador, editores
   pesados y sincronizadores de archivos que no formen parte del entorno
   controlado; anotar cualquier programa que deba permanecer abierto.
3. Ejecutar `diagnostico_entorno.py` y guardar la salida en `docs/entorno.md`.
4. Generar datos con semilla fija: `python -m src.generar_datos <n>`.

| Dato de la sesión | Valor |
|---|---|
| Fecha/hora de inicio y zona horaria | Registrar antes de cualquier sesión futura aprobada |
| Conexión a corriente; lectura de corriente, unidad e instrumento si disponibles | Registrar antes de cualquier sesión futura aprobada |
| Perfil de energía | Registrar antes de cualquier sesión futura aprobada |
| Programas abiertos al inicio y los que permanecen durante la prueba | Registrar antes de cualquier sesión futura aprobada |

No completar estos campos con valores supuestos. La medición del 18-11-2026
no registró programas abiertos ni condiciones de alimentación; esos datos
permanecen desconocidos. La serie 3 del 25-11-2026 se ejecutó en condiciones
controladas; el registro disponible confirma conexión a corriente, perfil
equilibrado y cierre general de procesos pesados, pero no enumera aplicaciones
ni confirma incidentes. Ver el registro separado en [entorno.md](entorno.md).

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
- Umbral: CV ≤ 10 % por combinación. Si se supera, inspeccionar bitácora de
  incidentes y valores individuales, calcular Tukey y reportar ambos resultados.
- No borrar datos sin una causa verificable y documentada; si no hay causa,
  conservar todas las repeticiones y declarar la limitación.
- La serie 3 controlada ya se realizó. El CV combinado de las tres series
  permanece >10 % en las nueve combinaciones A/B/C y n; se debe informar como
  limitación y tratar los resultados como exploratorios. No ejecutar otra
  serie automáticamente: solo considerar una nueva corrida si antes se
  identifica una condición concreta que se controlará y se registra su plan.
- Aplicación a `resultados.csv`: A n=1 000 y C en los tres tamaños superaron
  CV=10 %. Tukey marcó A n=4 000 repetición 1, C n=2 000 repetición 4 y
  C n=4 000 repetición 3. No se hallaron incidentes registrados en la bitácora,
  así que no se excluyó ninguna fila.
- El tiempo de C está en el orden de 0.1–0.6 ms y `process_time()` registra
  valores de 0.000000 s en esas corridas. La causa concreta no se aisló; se
  recomienda medir lotes de ejecuciones para una futura revisión.

## 6. Registro de incidentes
| Fecha/hora | Incidente (p. ej. actualización del SO, batería) | Corridas afectadas | Decisión |
|---|---|---|---|

Para la serie 3 no se registró un incidente específico. La ausencia de una
anotación no se interpreta como confirmación de que no ocurriera ninguno.
