# Plantilla de variables experimentales

| Tipo | Variable | Símbolo | Unidad | Valores / rango | Instrumento o forma de obtención | Justificación |
|---|---|---|---|---|---|---|
| Independiente | Estrategia | — | — | A, B, C | — | |
| Independiente | Tamaño de entrada | n | elementos | | — | |
| Dependiente | Tiempo de ejecución | t | s | — | time.perf_counter() | |
| Dependiente | Pico de memoria | M | MiB | — | tracemalloc (corrida separada) | |
| Dependiente | Uso de CPU | U | % | — | t_CPU / t | |
| Dependiente (opcional) | Temperatura | θ | °C | — | sensores.py | Plan B si no disponible: |
| Dependiente (opcional) | Energía | E | J | — | RAPL / vatímetro | Plan B si no disponible: |
| Controlada | Equipo | — | — | | diagnostico_entorno.py | |
| Controlada | Versión de Python | — | — | | | |
| Controlada | Alimentación (corriente/batería) | — | — | | | |
| Controlada | Programas abiertos | — | — | | | |
| Controlada | Datos de entrada (semilla) | — | — | | | |

## Mapa de dependencias
Describa con flechas qué variable influye en cuál, por ejemplo:
`Estrategia → número de operaciones → ciclos (N = f·t) → tiempo t`
`Estrategia → datos almacenados → pico de memoria M`

## Variables que NO controlamos y cómo las mitigamos
| Variable no controlada | Efecto posible | Mitigación (repeticiones, orden aleatorio, calentamiento...) |
|---|---|---|
| Frecuencia dinámica (turbo/ahorro) | | |
| Procesos del sistema operativo | | |
| Caché de archivos del SO | | |
