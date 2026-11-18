# Registro de decisiones técnicas (ADR breve)

Cada decisión importante se registra aquí y se enlaza desde el issue o PR correspondiente.

## D-001 — Estrategia C como índice directo
- **Fecha:** 2026-11-18 · **Autor(es):** Equipo 7 / Copilot SDK · **Issue/PR:** por crear
- **Contexto:** Estrategia-C representa la alternativa de índice directo cuando el catálogo crece.
- **Opciones consideradas:** 1) diccionario código -> producto; 2) lista de pares ordenada con búsqueda binaria.
- **Decisión:** Implementar un diccionario construido una vez por ejecución y acceso por clave para cada consulta.
- **Justificación:** El índice elimina el ordenamiento por inserción y evita recorridos lineales para las consultas.
- **Consecuencias / riesgos:** Consume memoria adicional proporcional a n y no debe confundirse el tamaño teórico promedio con una garantía de tiempo constante en todas las cargas.

## D-002 — _(título)_
- **Fecha:** · **Autor(es):** · **Issue/PR:** #
- **Contexto:** ¿qué problema o pregunta motivó la decisión?
- **Opciones consideradas:** 1) … 2) … 3) …
- **Decisión:**
- **Justificación (incluya evidencia o principio físico):**
- **Consecuencias / riesgos:**
