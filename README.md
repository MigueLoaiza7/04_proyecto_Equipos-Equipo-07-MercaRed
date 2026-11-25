# Equipo 7 — Algoritmos de búsqueda y ordenamiento

> Proyecto: *Laboratorio colaborativo de rendimiento y eficiencia computacional desde la física aplicada*
> Física Aplicada al Desarrollo de Software · SENA · ADSO · 7.º trimestre

## 1. Problema empresarial
**Empresa (caso simulado):** MercaRed Colombia, tienda en línea con catálogo en crecimiento

Con 5 000 productos la actualización del catálogo tardaba segundos; con 50 000 tarda varios minutos. La gerencia pregunta cuánto tardará con 500 000.

## 2. Situación inicial medible

`src/linea_base.py` ordena por inserción y busca cada código linealmente.
Medición formal de A (10 tiempos por caso):

| Tamaño n | Tiempo medio A | Unidad | Equipo y fecha |
|---:|---:|---|---|
| 1 000 | 0.042791 | s | Windows 10 / CPython 3.14.7, 18-11-2026 |
| 2 000 | 0.162089 | s | Windows 10 / CPython 3.14.7, 18-11-2026 |
| 4 000 | 0.662829 | s | Windows 10 / CPython 3.14.7, 18-11-2026 |

## 3. Pregunta de investigación

¿Cómo cambian el tiempo de pared (s) y el pico de memoria Python (MiB) al
reemplazar A por C y aumentar n, manteniendo el mismo equipo, versión de
Python, datos y consultas?

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
python -m experimentos.analizar_resultados resultados/resultados.csv
```

En Windows se puede usar `C:\Python314\python.exe` si el alias `python` no está
configurado.

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

**Medición real:** Windows 10, CPython 3.14.7, 8 núcleos lógicos; 10 tiempos
por grupo y una corrida de memoria aparte. En 1 000, 2 000 y 4 000 productos,
C midió 336×, 682× y 1 416× menos tiempo medio que A. A 4 000, C tardó
0.000468 s (IC 95 %: 0.000421–0.000515) frente a 0.662829 s
(0.638150–0.687509) de A. El pico Python de C fue 0.212 MiB contra 0.032 MiB
de A. Las mediciones no estiman rendimiento a 500 000 ni energía.

| n | A media s (IC 95 %) | CV A | Memoria A MiB | C media s (IC 95 %) | CV C | Memoria C MiB |
|---:|---:|---:|---:|---:|---:|---:|
| 1 000 | 0.042791 (0.039586–0.045996) | 10.47 % | 0.009 | 0.000128 (0.000115–0.000140) | 13.86 % | 0.054 |
| 2 000 | 0.162089 (0.153431–0.170747) | 7.47 % | 0.017 | 0.000238 (0.000204–0.000271) | 19.76 % | 0.106 |
| 4 000 | 0.662829 (0.638150–0.687509) | 5.21 % | 0.032 | 0.000468 (0.000421–0.000515) | 14.17 % | 0.212 |

Los CV superiores a 10 % se investigaron; tres corridas cumplen el criterio
Tukey de atípico. Como el protocolo no registra incidentes que expliquen esos
casos, no se eliminaron ni se les asignó una causa. El informe y el detalle se
encuentran en [docs/informe.md](docs/informe.md), [resultados/resumen.csv](resultados/resumen.csv)
y [resultados/atipicos.csv](resultados/atipicos.csv).

![Tiempo contra n, log-log e IC 95 %](resultados/tiempo_vs_n.svg)

![Comparación A/C en n mayor e IC 95 %](resultados/comparacion_n_mayor.svg)

Las hipótesis de tiempo se apoyan dentro del rango medido: C es más rápida y
su tiempo creció 1.86× y 1.97× al duplicar n. La memoria medida de C fue
aproximadamente 6.00×, 6.24× y 6.63× la de A. Se recomienda probar C para
consultas si el incremento de memoria es aceptable; medir 50 000 y 500 000
antes de planear capacidad. Frecuencia, temperatura y energía no estuvieron
disponibles: no se afirma ahorro energético ni se extrapola energía.

**Pregunta de 500 000 productos (estimación, no medición):** un ajuste log-log
de las medias de A para n=1 000, 2 000 y 4 000 estima 9 134 s (2,54 h). Es una
extrapolación 125× por encima del mayor n medido y supone que se mantiene la
tendencia observada; no es una duración garantizada ni evidencia sobre memoria
o energía. No se ejecutó A con 500 000 productos. Se reporta la estimación y
se reserva una medición directa para el caso de que la actividad la exija
explícitamente y se acuerde su programación.

**Próxima medición de A:** R1 coordina el protocolo y registra el entorno;
R4 prepara y ejecuta la medición y conserva sus resultados. Antes de empezar
se deben registrar fecha/hora, conexión a corriente (y lectura de corriente
solo si hay instrumento), perfil de energía y programas abiertos. Estos datos
no quedaron registrados en la medición del 18-11-2026 y no se reconstruyen a
posteriori. La coordinación corresponde a la [issue #1](https://github.com/MigueLoaiza7/04_proyecto_Equipos-Equipo-07-MercaRed/issues/1);
los valores de la próxima sesión siguen pendientes.

El resumen, atípicos, auditoría de campos y gráficos se reproducen con
`python -m experimentos.analizar_resultados resultados/resultados.csv`.
