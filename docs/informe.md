# Informe científico breve — Equipo __

**Título:** · **Integrantes:** · **Fecha:** · **Repositorio:**

## Resumen (≤ 150 palabras)
Problema, método, resultado principal con cifras y unidades, conclusión.

## 1. Introducción
Problema empresarial y pregunta de investigación. Principios físicos involucrados (con fórmulas y unidades).

## 2. Hipótesis
H1, H2... (copiadas de docs/hipotesis.md, sin modificarlas después de ver los datos).

## 3. Método
- Estrategias comparadas (descripción, no código completo).
- Variables independientes, dependientes y controladas.
- Entorno (tabla de docs/entorno.md). Instrumentos y su resolución.
- Protocolo: tamaños, repeticiones, calentamiento, orden aleatorio.

## 4. Resultados

Medición formal real: A línea base y C índice directo, 10 repeticiones de
tiempo por combinación y una corrida separada de memoria.

| Estrategia | n | Tiempo medio (s) | Desviación estándar (s) | CV (%) | IC95 % de la media (s) | Pico de memoria (MiB; 1 corrida) |
|---|---:|---:|---:|---:|---:|---:|
| A | 1 000 | 0.042791 | 0.004481 | 10.47 | [0.039586, 0.045996] | 0.009 |
| A | 2 000 | 0.162089 | 0.012104 | 7.47 | [0.153431, 0.170747] | 0.017 |
| A | 4 000 | 0.662829 | 0.034502 | 5.21 | [0.638150, 0.687509] | 0.032 |
| C | 1 000 | 0.000128 | 0.000018 | 13.86 | [0.000115, 0.000140] | 0.054 |
| C | 2 000 | 0.000238 | 0.000047 | 19.76 | [0.000204, 0.000271] | 0.106 |
| C | 4 000 | 0.000468 | 0.000066 | 14.17 | [0.000421, 0.000515] | 0.212 |

Los IC95 % son intervalos t de Student para la media (10 repeticiones, 9 grados
de libertad); la memoria tiene una sola corrida por combinación y no tiene
intervalo de confianza. C fue más rápida que A en tiempo para los tres tamaños,
pero su pico de memoria medido fue mayor. El criterio del protocolo (CV ≤ 10 %)
se supera en A para n = 1 000 y en C para los tres tamaños; esos resultados
requieren una repetición bajo condiciones estables y deben conservarse y
reportarse junto con la serie original. Frecuencia, temperatura, RSS y energía
no estuvieron disponibles.
- Gráfico 1: tiempo vs. n (log–log, barras de error).
- Gráfico 2: comparación de estrategias para el n mayor.
- (Si aplica) memoria, CPU %, temperatura, energía. **Marcar medido / estimado / simulado.**

## 5. Discusión
- ¿Se confirma o refuta cada hipótesis? Criterio usado.
- Explicación física de los resultados.
- Limitaciones de la medición y amenazas a la validez.

## 6. Propuesta de mejora para la empresa
Recomendación cuantificada, condiciones en que es válida y riesgos.

## 7. Conclusiones

## 8. Referencias (verificables)
## Anexo: uso de IA (resumen de docs/uso_ia.md)
