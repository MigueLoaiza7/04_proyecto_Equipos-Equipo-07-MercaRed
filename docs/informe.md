# Informe científico breve — Equipo 7

**Título:** Comparación de estrategias de búsqueda y ordenamiento para el catálogo MercaRed
**Integrantes:** nombres pendientes de confirmar · **Fecha:** 2026-11-25
**Repositorio:** MigueLoaiza7/04_proyecto_Equipos-Equipo-07-MercaRed

## Resumen

Se compararon A (inserción y búsqueda lineal), B (mezcla y búsqueda binaria) y
C (índice directo) en Windows 10, CPython 3.12.10, con la misma semilla, tres
tamaños y dos series de diez repeticiones. B y C tuvieron menores tiempos
medios que A en el rango de 1 000–4 000 productos; B usó menos memoria que C.
Sin embargo, las 20 muestras combinadas superaron CV 10 % en todas las
combinaciones. La medición es exploratoria: se conservan ambas series y se
requiere una sesión mejor controlada antes de conclusiones firmes o extrapolar
a 500 000 productos.

## 1. Introducción

La actualización de un catálogo creciente puede requerir ordenar productos y
atender consultas por código. La pregunta es cómo cambian el tiempo de pared y
el pico de memoria al usar estrategias con diferente crecimiento, manteniendo
el mismo catálogo, consultas, equipo, versión de Python y semilla. El trabajo
algorítmico esperado incluye términos O(n²), O(n log n), O(n) y O(log n);
los tiempos reales dependen además de frecuencia, caché y carga del sistema.

## 2. Hipótesis

H1–H4 están registradas en [docs/hipotesis.md](./hipotesis.md). H4 predice que
B reducirá al menos 50 % el tiempo medio frente a A para n = 4 000; la
comparación observada está en Resultados, pero la dispersión obliga a tratarla
como evidencia provisional.

## 3. Método

- **A:** ordenamiento por inserción y búsqueda lineal.
- **B:** ordenamiento por mezcla iterativa de una copia del catálogo y búsqueda binaria.
- **C:** diccionario código-producto, construido dentro de cada ejecución.
- Se usaron tamaños n = 1 000, 2 000 y 4 000, semilla 7, orden aleatorio con
  semilla 42, calentamiento y preparación de datos fuera del cronómetro.
- Se hicieron dos series independientes de 10 tiempos por estrategia y tamaño.
  Cada combinación tuvo una corrida separada de memoria por serie.
- Tiempo medido con `time.perf_counter`; pico de memoria Python con
  `tracemalloc`. Las limitaciones del entorno se detallan en [docs/entorno.md](./entorno.md).
- Las dos series se conservaron por separado; el resumen adicional agrupa sus
  20 tiempos sin descartar datos.

## 4. Resultados

Comparación formal A/B/C del 25-11-2026. Valores agrupados de ambas series
(20 tiempos por combinación); IC95 % t de Student con 19 grados de libertad.
La memoria es el promedio de dos corridas separadas de `tracemalloc`, no una
medición repetida para calcular un intervalo.

| Estrategia | n | Media t (s) | Desv. estándar (s) | CV (%) | IC95 % t (s) | Pico Python medio (MiB) |
|---|---:|---:|---:|---:|---:|---:|
| A | 1 000 | 0.044441 | 0.007026 | 15.81 | [0.041153, 0.047729] | 0.009 |
| A | 2 000 | 0.170146 | 0.029874 | 17.56 | [0.156165, 0.184128] | 0.017 |
| A | 4 000 | 0.751516 | 0.114270 | 15.21 | [0.698036, 0.804995] | 0.032 |
| B | 1 000 | 0.005322 | 0.008376 | 157.41 | [0.001401, 0.009242] | 0.016 |
| B | 2 000 | 0.007765 | 0.001272 | 16.38 | [0.007169, 0.008360] | 0.032 |
| B | 4 000 | 0.019949 | 0.011667 | 58.49 | [0.014489, 0.025410] | 0.062 |
| C | 1 000 | 0.000139 | 0.000047 | 34.02 | [0.000117, 0.000161] | 0.054 |
| C | 2 000 | 0.000237 | 0.000059 | 24.78 | [0.000210, 0.000264] | 0.106 |
| C | 4 000 | 0.000497 | 0.000128 | 25.70 | [0.000437, 0.000557] | 0.212 |

La pendiente log-log calculada sobre las medias agrupadas es A = 2.04,
B = 0.95 y C = 0.92 para el rango medido. La media de B en n = 4 000 fue
97.34 % menor que A, por lo que satisface la predicción puntual de H4; no se
considera concluyente porque CV de B fue 58.49 %. El criterio CV ≤ 10 % no se
alcanzó en ninguna combinación agrupada; las CV por serie se encuentran en
[resultados/resumen_estadistico_A_B_C.csv](../resultados/resumen_estadistico_A_B_C.csv).

**Gráfico 1:** [tiempo vs. n, ejes log-log e IC95 %](../resultados/grafico_tiempo_loglog.png)
**Gráfico 2:** [comparación para n = 4 000 e IC95 %](../resultados/grafico_estrategias_n_mayor.png)

La primera serie de B en n = 1 000 contiene una observación de 0.040827 s,
mientras las otras nueve estuvieron entre 0.002972 y 0.003459 s. No se conoce
la causa; se conservó y no se descartó como atípica. La segunda serie de esa
combinación tuvo CV 20.78 %. Tampoco se registraron aplicaciones abiertas ni
perfil de energía, por lo que la carga del equipo es una limitación. No hubo
sensores disponibles para frecuencia, temperatura, RSS o energía; no se afirma
ahorro energético.

Como referencia histórica independiente, el 18-11-2026 se midieron A y C con
CPython 3.14.7; esos datos no se mezclan ni comparan en tiempos absolutos con
esta serie CPython 3.12.10.

## 5. Discusión

Los promedios muestran B y C más rápidos que A. H1 recibe apoyo descriptivo,
pero no se confirma estadísticamente con la dispersión observada. Para H2, C
creció 1.71× y 2.10× al duplicar n, dentro del intervalo previsto; es
compatible con crecimiento lineal, aunque tres tamaños y CV altos no prueban
complejidad asintótica. H3 recibe apoyo: C usó 0.054/0.106/0.212 MiB frente a
0.009/0.017/0.032 MiB de A. La pendiente empírica de B y C no demuestra por sí
sola complejidad asintótica. B requiere memoria auxiliar para ordenar; C usa
más memoria por el índice. H4 cumple el umbral puntual, pero debe repetirse
con carga controlada porque se incumplió el criterio de dispersión.

## 6. Propuesta de mejora para la empresa

Evaluar B como alternativa de catálogo general y C cuando el coste adicional
de memoria sea aceptable. Antes de seleccionar una solución o extrapolar a
500 000 productos, repetir el experimento en condiciones registradas, ampliar
el rango de n y medir memoria de proceso además de `tracemalloc`.

## 7. Conclusiones

La verificación funcional confirma que A, B y C devuelven el mismo número de
consultas encontradas. En esta máquina y rango, B y C presentan menores medias
de tiempo, con mayor memoria para C; la dispersión excede el criterio fijado,
así que el resultado es preliminar y requiere nuevas mediciones controladas.

## 8. Referencias

- Python `time.perf_counter`: https://docs.python.org/3/library/time.html#time.perf_counter
- Python `tracemalloc`: https://docs.python.org/3/library/tracemalloc.html
- Registro de mediciones y fuente CSV: `resultados/resultados_A_B_C_serie1.csv` y `resultados/resultados_A_B_C_serie2.csv`.

## Anexo: uso de IA

Ver [docs/uso_ia.md](./uso_ia.md); revisar y completar la reflexión individual antes de la sustentación.
