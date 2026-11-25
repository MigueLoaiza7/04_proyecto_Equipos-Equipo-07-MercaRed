# Equipo 7 — Algoritmos de búsqueda y ordenamiento

> Proyecto: *Laboratorio colaborativo de rendimiento y eficiencia computacional desde la física aplicada*
> Física Aplicada al Desarrollo de Software · SENA · ADSO · 7.º trimestre

## 1. Problema empresarial
**Empresa (caso simulado):** MercaRed Colombia, tienda en línea con catálogo en crecimiento

Con 5 000 productos la actualización del catálogo tardaba segundos; con 50 000 tarda varios minutos. La gerencia pregunta cuánto tardará con 500 000.

## 2. Situación inicial medible
src/linea_base.py ordena por inserción y busca cada código linealmente.

| Medición preliminar (Clase 3) | Valor | Unidad |
|---|---|---|
| n utilizado | | registros |
| Tiempo de ejecución (1 corrida) | | s |
| Equipo y fecha | | — |

## 3. Pregunta de investigación
_¿Cómo cambia ________ (VD, unidad) cuando ________ (VI), manteniendo ________ (VC)?_

## 4. Hipótesis
Ver [docs/hipotesis.md](docs/hipotesis.md).

## 5. Estrategias
| Id | Estrategia | Idea principal | Resultado esperado | Estado |
|---|---|---|---|---|
| A | Línea base | Inserción y búsqueda lineal | Referencia correcta | Implementada |
| B | Mezcla + búsqueda binaria | Ordena por código y busca por intervalo | Menor crecimiento del trabajo que A; memoria auxiliar adicional | Implementada |
| C | Índice directo | Diccionario código -> producto | Evitar ordenamiento y recorridos lineales | Implementada |

La Estrategia B ordena una copia del catálogo con mezcla iterativa y resuelve
las consultas con búsqueda binaria. La Estrategia C construye un índice de
código a producto y usa cada consulta como clave; no modifica el catálogo
recibido, pero almacena una referencia adicional por producto.

## 6. Cómo reproducir
```bash
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt                          # matplotlib para gráficos; psutil es opcional
python -m src.linea_base                                 # situación inicial
python -m unittest discover -s pruebas                   # corrección
python -m experimentos.ejecutar_experimento --salida resultados/resultados_A_B_C_serie1.csv
# Si el CV supera 10 %, conservar la primera serie y repetir en archivo separado:
python -m experimentos.ejecutar_experimento --salida resultados/resultados_A_B_C_serie2.csv --observacion "serie adicional CV"
python -m experimentos.ejecutar_experimento --salida resultados/resultados_A_B_C_serie3.csv --observacion "serie controlada"
python -m experimentos.analizar_resultados resultados/resultados_A_B_C_serie1.csv resultados/resultados_A_B_C_serie2.csv resultados/resultados_A_B_C_serie3.csv
```

El resumen incluye media, desviación estándar, CV, IC95 % y pendiente log-log.
Los gráficos se generan en `resultados/grafico_tiempo_loglog.png` y
`resultados/grafico_estrategias_n_mayor.png`.

## 7. Integrantes y roles
| Rol | Integrante | Responsabilidad principal |
|---|---|---|
| R1 — Coordinación y protocolo experimental | Integrante A | Mantiene el protocolo y la bitácora de decisiones; controla variables; modera issues y la planeación. |
| R2 — Desarrollo de estrategia base | Integrante B | Comprende y documenta la línea base; asegura la verificación de corrección (pruebas) de todas las estrategias. |
| R3 — Estrategias alternativas y optimización | Integrantes B y C | Diseñan e implementan estrategias alternativas y justifican sus efectos. |
| R4 — Automatización de mediciones y análisis | Integrantes A y C | Automatizan experimentos y registro CSV; producen estadísticas y gráficos; documentan el entorno. |

Los roles son flexibles: **todos** participan en la comprensión física y en el código.

## 8. Documentación
- [Variables](docs/variables.md) · [Protocolo](docs/protocolo.md) · [Entorno](docs/entorno.md)
- [Decisiones técnicas](docs/decisiones.md) · [Uso de IA](docs/uso_ia.md) · [Informe](docs/informe.md)

## 9. Resultados y conclusiones (Clase 5)
Resumen: en las tres series A/B/C del 25-11-2026 (30 tiempos combinados por
estrategia/tamaño), B y C tuvieron menores tiempos medios que A entre 1 000 y
4 000 productos. Una tercera serie controlada mejoró algunas combinaciones,
pero todas las CV combinadas aún exceden 10 %; los resultados siguen siendo
exploratorios. Detalles, intervalos y limitaciones están en
[docs/informe.md](docs/informe.md). No se extrapola a 500 000 productos.

### Estrategia C

Los resultados A/C de noviembre 18 son históricos y corresponden a CPython
3.14.7; no se mezclan con la nueva comparación A/B/C ejecutada con CPython
3.12.10.

Ejecución formal real completada el 18-11-2026 en Windows 10 con CPython
3.14.7, AMD64 y 8 núcleos lógicos. Se midieron A y C con 10 repeticiones de
tiempo por tamaño y una corrida separada de memoria por combinación.

| n | A media (s) | C media (s) | C memoria (MiB) |
|---|---:|---:|---:|
| 1 000 | 0.042791 | 0.000128 | 0.054 |
| 2 000 | 0.162089 | 0.000238 | 0.106 |
| 4 000 | 0.662829 | 0.000468 | 0.212 |

La media de C fue aproximadamente 334 veces menor que A en n=1 000, 681 veces
en n=2 000 y 1 416 veces en n=4 000. Al duplicar n, C pasó de 0.000128 s a
0.000238 s y luego a 0.000468 s, crecimiento cercano a 2×, compatible con
construcción lineal del índice dentro del rango medido. C usó 0.054, 0.106 y
0.212 MiB, aproximadamente 6×, 6.24× y 6.63× la memoria trazada de A.

Estos datos históricos se conservan en `resultados/resultados.csv`. La
comparación A/B/C de noviembre 25 está en los tres CSV de serie y en
`resultados/resumen_estadistico_A_B_C.csv`. Las corridas con `tracemalloc`
están separadas de las mediciones de tiempo y no deben interpretarse como
tiempos normales.

Las hipótesis y variables están documentadas en
[docs/hipotesis.md](docs/hipotesis.md) y
[docs/variables.md](docs/variables.md). Sin RAPL, vatímetro o medición eléctrica
equivalente no se afirma consumo o ahorro energético.
