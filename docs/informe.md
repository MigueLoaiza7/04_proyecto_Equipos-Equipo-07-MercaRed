# Informe científico breve — Equipo 7

**Título:** Comparación de estrategias de búsqueda y ordenamiento para el catálogo MercaRed
**Integrantes:** A, B y MigueLoaiza7 (C); nombres completos de A y B pendientes · **Fecha:** 2026-11-25
**Repositorio:** MigueLoaiza7/04_proyecto_Equipos-Equipo-07-MercaRed

## Resumen

Se compararon A (inserción y búsqueda lineal), B (mezcla y búsqueda binaria) y
C (índice directo) en Windows 10, CPython 3.12.10, con la misma semilla, tres
tamaños y tres series de diez repeticiones. B y C tuvieron menores tiempos
medios que A en el rango de 1 000–4 000 productos; B usó menos memoria que C.
La tercera serie se hizo bajo condiciones controladas.
Aun así, las 30 muestras combinadas superaron CV 10 % en todas las
combinaciones. La medición sigue siendo exploratoria y no permite extrapolar
con confianza a 500 000 productos.

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
- Se hicieron tres series independientes de 10 tiempos por estrategia y tamaño.
  Cada combinación tuvo una corrida separada de memoria por serie.
- Tiempo medido con `time.perf_counter`; pico de memoria Python con
  `tracemalloc`. Las limitaciones del entorno se detallan en [docs/entorno.md](./entorno.md).
- Las tres series se conservaron por separado; el resumen adicional agrupa sus
  30 tiempos sin descartar datos. La tercera serie se identificó como controlada
  después de CV altos en las dos primeras.

## 4. Resultados

Comparación formal A/B/C del 25-11-2026. Valores agrupados de las tres series
(30 tiempos por combinación); IC95 % t de Student con 29 grados de libertad.
La memoria es el promedio de tres corridas separadas de `tracemalloc`, no una
medición repetida para calcular un intervalo.

| Estrategia | n | Media t (s) | Desv. estándar (s) | CV (%) | IC95 % t (s) | Pico Python medio (MiB) |
|---|---:|---:|---:|---:|---:|---:|
| A | 1 000 | 0.042623 | 0.006849 | 16.07 | [0.040066, 0.045180] | 0.009 |
| A | 2 000 | 0.160936 | 0.029517 | 18.34 | [0.149915, 0.171956] | 0.017 |
| A | 4 000 | 0.687086 | 0.131305 | 19.11 | [0.638061, 0.736110] | 0.032 |
| B | 1 000 | 0.004617 | 0.006863 | 148.65 | [0.002055, 0.007180] | 0.016 |
| B | 2 000 | 0.007796 | 0.001480 | 18.98 | [0.007244, 0.008349] | 0.032 |
| B | 4 000 | 0.018019 | 0.009882 | 54.84 | [0.014329, 0.021709] | 0.062 |
| C | 1 000 | 0.000132 | 0.000040 | 30.47 | [0.000117, 0.000147] | 0.054 |
| C | 2 000 | 0.000227 | 0.000051 | 22.34 | [0.000208, 0.000246] | 0.106 |
| C | 4 000 | 0.000477 | 0.000111 | 23.27 | [0.000436, 0.000519] | 0.212 |

La pendiente log-log calculada sobre las medias agrupadas es A = 2.01,
B = 0.98 y C = 0.93 para el rango medido. La media de B en n = 4 000 fue
97.38 % menor que A, por lo que satisface la predicción puntual de H4; no se
considera concluyente porque CV de B fue 54.84 %. El criterio CV ≤ 10 % no se
alcanzó en ninguna combinación agrupada; las CV por serie se encuentran en
[resultados/resumen_estadistico_A_B_C.csv](../resultados/resumen_estadistico_A_B_C.csv).

**Gráfico 1:** [tiempo vs. n, ejes log-log e IC95 %](../resultados/grafico_tiempo_loglog.png)
**Gráfico 2:** [comparación para n = 4 000 e IC95 %](../resultados/grafico_estrategias_n_mayor.png)

La primera serie de B en n = 1 000 contiene una observación de 0.040827 s,
mientras las otras nueve estuvieron entre 0.002972 y 0.003459 s. No se conoce
la causa; se conservó y no se descartó como atípica. La segunda serie de esa
combinación tuvo CV 20.78 %. En la tercera serie, realizada tras confirmarse
corriente, perfil equilibrado y cierre de aplicaciones pesadas, dos de nueve
combinaciones quedaron bajo CV 10 %; el CV combinado siguió superando el umbral
en las nueve. La confirmación de las condiciones fue manual, no sensorizada.
No hubo sensores disponibles para frecuencia, temperatura, RSS o energía; no
se afirma ahorro energético.

Como referencia histórica independiente, el 18-11-2026 se midieron A y C con
CPython 3.14.7; esos datos no se mezclan ni comparan en tiempos absolutos con
esta serie CPython 3.12.10.

## 5. Discusión

Los promedios muestran B y C más rápidos que A. H1 recibe apoyo descriptivo,
pero no se realizó una prueba inferencial de diferencia entre estrategias y la
dispersión impide una conclusión firme. Para H2, C creció 1.72× y 2.10× al
duplicar n, dentro del intervalo previsto; esto es compatible con crecimiento
lineal, aunque tres tamaños y CV altos no prueban complejidad asintótica. H3
recibe apoyo: C usó 0.054/0.106/0.212 MiB frente a 0.009/0.017/0.032 MiB de A.
La pendiente empírica de B y C tampoco demuestra por sí sola complejidad
asintótica. B requiere memoria auxiliar para ordenar; C usa más memoria por el
índice. H4 cumple el umbral puntual, pero los resultados siguen siendo
exploratorios porque el CV combinado excede el criterio.

## 6. Propuesta de mejora para la empresa

Evaluar B como alternativa de catálogo general y C cuando el coste adicional
de memoria sea aceptable. Antes de seleccionar una solución o extrapolar a
500 000 productos, repetir el experimento en condiciones registradas, ampliar
el rango de n y medir memoria de proceso además de `tracemalloc`.

## 7. Conclusiones

La verificación funcional confirma que A, B y C devuelven el mismo número de
consultas encontradas. En esta máquina y rango, B promedió 0.018019 s frente a
0.687086 s de A en n = 4 000, pero CV combinado fue 54.84 %. C también tuvo
menores medias y mayor memoria trazada que A. La dispersión excede el criterio,
así que el resultado sigue siendo preliminar y no se extrapola a 500 000.

## 8. Referencias

- Python `time.perf_counter`: https://docs.python.org/3/library/time.html#time.perf_counter
- Python `tracemalloc`: https://docs.python.org/3/library/tracemalloc.html
- Registro de mediciones y fuente CSV: `resultados/resultados_A_B_C_serie1.csv`,
  `resultados/resultados_A_B_C_serie2.csv` y
  `resultados/resultados_A_B_C_serie3.csv`.

## Anexo: uso de IA

Ver [docs/uso_ia.md](./uso_ia.md); revisar y completar la reflexión individual antes de la sustentación.
