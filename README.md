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
| Id | Estrategia | Idea principal | Efecto físico esperado | Responsable |
|---|---|---|---|---|
| A | Línea base | (situación inicial) | — | R2 |
| B | | | | R3 |
| C | | | | R3 |

## 6. Cómo reproducir
```bash
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt                          # opcional: psutil, matplotlib
python -m src.linea_base                                 # situación inicial
python -m unittest discover -s pruebas                   # corrección
python -m experimentos.ejecutar_experimento              # experimento formal -> resultados/resultados.csv
python ruta/a/analizar_resultados.py resultados/resultados.csv
```

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
