# Registro de decisiones técnicas (ADR breve)

Cada decisión importante se registra aquí y se enlaza desde el issue o PR correspondiente.

## D-001 — Estrategia C como índice directo
- **Fecha:** 2026-11-18 · **Autor(es):** Equipo 7 / Copilot SDK · **Issue/PR:** por crear
- **Contexto:** Estrategia-C representa la alternativa de índice directo cuando el catálogo crece.
- **Opciones consideradas:** 1) diccionario código -> producto; 2) lista de pares ordenada con búsqueda binaria.
- **Decisión:** Implementar un diccionario construido una vez por ejecución y acceso por clave para cada consulta.
- **Justificación:** El índice elimina el ordenamiento por inserción y evita recorridos lineales para las consultas.
- **Consecuencias / riesgos:** Consume memoria adicional proporcional a n y no debe confundirse el tamaño teórico promedio con una garantía de tiempo constante en todas las cargas.

## D-002 — Análisis reproducible sin dependencias opcionales
- **Fecha:** 2026-11-25 · **Autor(es):** Equipo 7 / Copilot SDK · **Issue/PR:** por crear
- **Contexto:** Los scripts de Clase 5 referenciados en las instrucciones no estaban disponibles en el repositorio ni en el entorno local.
- **Opciones consideradas:** 1) dejar el análisis sin ejecutar; 2) estimar resultados manualmente; 3) añadir un analizador reproducible con biblioteca estándar.
- **Decisión:** Crear `experimentos/analizar_resultados.py` para auditar el CSV, resumir medias/CV/IC 95 % t, identificar Tukey y producir SVG.
- **Justificación:** El CSV contiene 10 repeticiones por combinación; con df=9 el IC usa t=2.262. No requiere instalar paquetes ni ocultar la falta de los scripts oficiales.
- **Consecuencias / riesgos:** El informe es equivalente y rastreable, pero no se presenta como salida de `analizar_resultados.py` o `verificar_hipotesis.py` oficiales. Los resultados no se filtraron por CV o Tukey.

## D-003 — Reporte independiente para Estrategia C
- **Fecha:** 2026-11-25 · **Autor(es):** Equipo 7 / Copilot SDK · **Issue/PR:** por crear
- **Contexto:** C requiere explicar costo del índice, memoria adicional y riesgo de claves duplicadas sin duplicar la conclusión de A.
- **Opciones consideradas:** 1) conservar solo la comparación conjunta; 2) agregar un informe y artefactos filtrados para C manteniendo A como referencia.
- **Decisión:** El informe de esta rama se enfoca en C y el analizador produce CSV/gráfico por estrategia; A permanece únicamente como comparador cuantitativo.
- **Justificación:** El tiempo medido de C incluye construir el índice y consultar; las tendencias y limitaciones deben corresponder a ese mecanismo y sus propios datos.
- **Consecuencias / riesgos:** La etiqueta `v1.0` ya apunta al cierre de Estrategia-A; se conserva y el cierre de C usa una etiqueta distinta.
