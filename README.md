# Equipo 7 — Algoritmos de búsqueda y ordenamiento

> Proyecto: *Laboratorio colaborativo de rendimiento y eficiencia computacional desde la física aplicada*
> Física Aplicada al Desarrollo de Software · SENA · ADSO · 7.º trimestre

## 1. Problema empresarial
**Empresa (caso simulado):** MercaRed Colombia, tienda en línea con catálogo en crecimiento

Con 5 000 productos la actualización del catálogo tardaba segundos; con 50 000 tarda varios minutos. La gerencia pregunta cuánto tardará con 500 000.

## 2. Situación inicial medible
`src/linea_base.py` ordena por inserción y busca cada código linealmente. Primera
evidencia obtenida con `python -m src.linea_base`:

| n (registros) | Consultas encontradas | Tiempo (1 corrida, s) |
|---:|---:|---:|
| 1.000 | 80 | 0,046 |
| 2.000 | 149 | 0,218 |
| 4.000 | 318 | 1,251 |

**Equipo y fecha:** AMD Ryzen 5 PRO 2400G with Radeon Vega Graphics · Windows 10
· Python 3.12.10 · 2026-11-18. Son mediciones preliminares de una corrida por
tamaño, no resultados estadísticos.

## 3. Pregunta de investigación
_¿Cómo cambia ________ (VD, unidad) cuando ________ (VI), manteniendo ________ (VC)?_

## 4. Hipótesis
Ver [docs/hipotesis.md](docs/hipotesis.md).

## 5. Estrategias
| Id | Estrategia | Idea principal | Resultado esperado | Estado |
|---|---|---|---|---|
| A | Línea base | Inserción y búsqueda lineal | Referencia correcta | Implementada |
| B | Pendiente | Alternativa por asignar | Comparación futura | Pendiente |
| C | Índice directo | Diccionario código -> producto | Evitar ordenamiento y recorridos lineales | Implementada |

La Estrategia C construye un índice de código a producto y usa cada consulta
como clave de búsqueda. No modifica el catálogo recibido ni requiere ordenar
los datos. Su costo principal es recorrer el catálogo una vez para construir el
índice y almacenar una referencia adicional por producto.

## 6. Cómo reproducir
```bash
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt                          # opcional: psutil, matplotlib
python -m src.linea_base                                 # situación inicial
python -m unittest discover -s pruebas                   # corrección
python -m experimentos.ejecutar_experimento              # experimento formal -> resultados/resultados.csv
python ruta/a/analizar_resultados.py resultados/resultados.csv
```

Las pruebas validan la línea base y comparan cada estrategia registrada en
`ESTRATEGIAS` con ella usando datos reproducibles y casos límite. Registra una
estrategia alternativa en `experimentos/ejecutar_experimento.py` para incluirla
automáticamente en esta verificación. La Estrategia B algorítmica sigue
pendiente; el rol del Integrante B es mantener la línea base y verificar la
corrección de las alternativas implementadas por el equipo.

## 7. Integrantes y roles
| Rol | Integrante | Responsabilidad principal |
|---|---|---|
| R1 — Coordinación y protocolo experimental | _(nombre)_ | Mantiene el protocolo y la bitácora de decisiones; controla variables; modera issues y la planeación. |
| R2 — Desarrollo de estrategia base | _(nombre)_ | Comprende y documenta la línea base; asegura la verificación de corrección (pruebas) de todas las estrategias. |
| R3 — Estrategias alternativas y optimización | _(nombre)_ | Diseña e implementa las estrategias alternativas y justifica físicamente por qué deberían cambiar las magnitudes. |
| R4 — Automatización de mediciones y análisis | _(nombre)_ | Automatiza experimentos y registro CSV; produce estadísticas y gráficos; documenta el entorno. |

Los roles son flexibles: **todos** participan en la comprensión física y en el código.

## 8. Documentación
- [Variables](docs/variables.md) · [Protocolo](docs/protocolo.md) · [Entorno](docs/entorno.md)
- [Decisiones técnicas](docs/decisiones.md) · [Uso de IA](docs/uso_ia.md) · [Informe](docs/informe.md)

## 9. Resultados y conclusiones (Clase 5)
_Resumen de máximo 5 líneas con cifras, unidades e intervalo de confianza._

### Estrategia C

Ejecución formal real completada el 18-11-2026 en Windows 10 con CPython
3.14.7, AMD64 y 8 núcleos lógicos. Se midieron A y C con 10 repeticiones de
tiempo por tamaño y una corrida separada de memoria por combinación.

Estas mediciones de A y C se realizaron en el mismo entorno y son la
comparación formal. Las mediciones preliminares de la sección 2 se ejecutaron
con Python 3.12.10 y en otro equipo; no deben compararse directamente con estos
resultados.

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

Los resultados se consideran reales únicamente cuando aparecen en
`resultados/resultados.csv`, generado por el experimento. Las corridas con
`tracemalloc` están separadas de las mediciones de tiempo y no deben
interpretarse como tiempos normales.

Las hipótesis y variables están documentadas en
[docs/hipotesis.md](docs/hipotesis.md) y
[docs/variables.md](docs/variables.md). Sin RAPL, vatímetro o medición eléctrica
equivalente no se afirma consumo o ahorro energético.
