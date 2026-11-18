# Informe científico breve — Equipo 7

**Título:** Medición preliminar de la Estrategia A en MercaRed Colombia
**Integrantes:** por completar · **Fecha:** 18-11-2026
**Repositorio:** MigueLoaiza7/04_proyecto_Equipos-Equipo-07-MercaRed

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

Medición real formal: Windows 10, CPython 3.14.7, AMD64, 8 núcleos lógicos,
10 repeticiones de tiempo por tamaño y una corrida separada de memoria.

| n | Media tiempo (s) | Mediana tiempo (s) | Pico Python (MiB) |
|---|---:|---:|---:|
| 1 000 | 0.046132 | 0.044608 | 0.009 |
| 2 000 | 0.206951 | 0.190294 | 0.017 |
| 4 000 | 0.724332 | 0.702276 | 0.032 |

Al duplicar de 1 000 a 2 000, el tiempo medio creció 4.49 veces; de 2 000 a
4 000 creció 3.50 veces. La memoria trazada creció 1.89 veces y 1.88 veces en
cada duplicación. Frecuencia, temperatura, RSS y energía no estuvieron
disponibles y no se estimaron.
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
