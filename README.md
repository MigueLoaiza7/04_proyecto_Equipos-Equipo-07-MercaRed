# Equipo 7 — Algoritmos de búsqueda y ordenamiento

Proyecto: *Laboratorio colaborativo de rendimiento y eficiencia computacional desde la física aplicada*

Física Aplicada al Desarrollo de Software · SENA · ADSO · 7.º trimestre

## Problema empresarial

MercaRed Colombia gestiona un catálogo que creció de 5 000 a 50 000 productos.
La gerencia necesita estimar el costo de atender el catálogo y las consultas
cuando llegue a 500 000 registros.

## Estrategia A implementada

La estrategia A corresponde a la línea base identificada por la rama
`Estrategia-A` y por la tabla original del proyecto:

- Ordenamiento por inserción: `src/estrategia_a.py`
- Búsqueda lineal por código sobre el catálogo ya ordenado
- Resultado equivalente a la línea base: número de consultas encontradas
- Complejidad esperada: ordenamiento cercano a O(n²) y búsqueda lineal O(n)
  por consulta, según el estado y distribución de los datos

La implementación conserva `preparar(n)` y `ejecutar(datos)`. `preparar(n)`
genera datos fuera del cronómetro y `ejecutar(datos)` contiene el trabajo medido.

## Ejecutar

Desde Windows PowerShell, usando el ejecutable real de Python:

```powershell
C:\Python314\python.exe -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt

python -m src.linea_base
python -m unittest discover -s pruebas
python -m experimentos.ejecutar_experimento --rapido
python -m experimentos.ejecutar_experimento
```

La ejecución rápida usa un tamaño y dos repeticiones. La ejecución formal usa
los tamaños 1 000, 2 000 y 4 000 con diez repeticiones de tiempo y una corrida
de memoria por caso. El plan se baraja con semilla 42 y los datos con semilla 7.

## Evidencia y medición

Los resultados se escriben en `resultados/resultados.csv`. Las condiciones del
proceso y del equipo se escriben junto a él en
`resultados/resultados.entorno.json`. Las medidas disponibles son:

- Tiempo de pared: `time.perf_counter()`, en segundos
- Tiempo de proceso: `time.process_time()`, en segundos
- Uso de CPU: cociente CPU/pared, en porcentaje
- Pico Python: `tracemalloc`, en MiB, en corrida separada
- RSS: memoria residente del proceso, en MiB
- Frecuencia y temperatura si el sistema las expone

No se afirma ahorro energético: RAPL o vatímetro no están disponibles de forma
garantizada y el porcentaje de CPU no representa potencia eléctrica.

## Pregunta e hipótesis

¿Cómo cambia el tiempo de ejecución y la memoria de A cuando crece `n`,
manteniendo semilla, equipo, consultas y versión de Python?

Las hipótesis verificables están en [docs/hipotesis.md](docs/hipotesis.md).
Variables y controles están en [docs/variables.md](docs/variables.md); el
procedimiento completo está en [docs/protocolo.md](docs/protocolo.md).

## Estado de los resultados

La existencia de un CSV indica medición real, no una simulación. Los campos
vacíos de frecuencia, temperatura o energía significan que el sensor no estaba
disponible y no deben sustituirse por estimaciones. El entorno usado se resume
en [docs/entorno.md](docs/entorno.md) y el JSON generado conserva el detalle
de máquina y Python.

Los resultados obtenidos no deben extrapolarse a 500 000 productos sin medir
ese rango. Para publicar una conclusión definitiva deben existir las
mediciones formales y la revisión en pull request.

### Medición formal real ejecutada

La ejecución formal terminó el 18-11-2026 en Windows 10 con CPython 3.14.7,
AMD64 y 8 núcleos lógicos. El CSV contiene 30 corridas de tiempo y 3 corridas
separadas de memoria. Las medias reales fueron:

| n | Tiempo medio de pared (s) | Mediana (s) | Pico Python (MiB) |
|---|---:|---:|---:|
| 1 000 | 0.046132 | 0.044608 | 0.009 |
| 2 000 | 0.206951 | 0.190294 | 0.017 |
| 4 000 | 0.724332 | 0.702276 | 0.032 |

Al duplicar de 1 000 a 2 000 registros, el tiempo medio creció aproximadamente
4.49 veces; al duplicar de 2 000 a 4 000, aproximadamente 3.50 veces. Esto es
compatible con un crecimiento superlineal dentro del rango medido, pero no
permite afirmar una pendiente cuadrática exacta con tres puntos ni extrapolar
a 500 000. Los picos medidos con `tracemalloc` fueron 0.009, 0.017 y 0.032 MiB.
Frecuencia, temperatura, RSS con `psutil` y energía RAPL no estuvieron
disponibles; sus campos aparecen vacíos y no se estimaron.

## Documentación

- [Hipótesis](docs/hipotesis.md)
- [Variables](docs/variables.md)
- [Protocolo](docs/protocolo.md)
- [Entorno](docs/entorno.md)
- [Decisiones técnicas](docs/decisiones.md)
- [Uso de IA](docs/uso_ia.md)
- [Informe](docs/informe.md)

## Integración colaborativa

El trabajo de Estrategia-A se desarrolla en una rama separada y debe integrarse
mediante pull request hacia `main`. Antes del merge se deben ejecutar pruebas,
prueba de humo y revisión del CSV; otro integrante debe comprobar que los
archivos documentados corresponden a las ejecuciones reales.
