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

| n | A media (s) | C media (s) | A pico (MiB) | C pico (MiB) |
|---|---:|---:|---:|---:|
| 1 000 | 0.042791 | 0.000128 | 0.009 | 0.054 |
| 2 000 | 0.162089 | 0.000238 | 0.017 | 0.106 |
| 4 000 | 0.662829 | 0.000468 | 0.032 | 0.212 |

C fue más rápida en las tres magnitudes. Al duplicar n su tiempo medio creció
aproximadamente de 1.86× y 1.97×. Su pico creció aproximadamente de 1.96× y
2.00×. Frecuencia, temperatura, RSS y energía no estuvieron disponibles.
- Tabla resumen: media, desviación, CV, IC95 % por estrategia y n.
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
