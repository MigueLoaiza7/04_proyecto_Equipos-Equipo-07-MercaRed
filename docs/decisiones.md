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

## D-003 — Mezcla y búsqueda binaria como Estrategia B
- **Fecha:** 2026-11-25 · **Autor(es):** MigueLoaiza7 (Integrante C) · **Issue/PR:** #3
- **Contexto:** Se requieren tres estrategias comparables para contrastar distintos crecimientos del trabajo.
- **Opciones consideradas:** 1) mezcla con búsqueda binaria; 2) quicksort con búsqueda binaria; 3) conservar C como tercera estrategia.
- **Decisión:** Ordenar una copia del catálogo con mezcla iterativa y buscar cada código con búsqueda binaria.
- **Justificación:** El ordenamiento cuesta O(n log n) y cada consulta O(log n), frente al ordenamiento por inserción O(n²) y las consultas lineales O(n).
- **Consecuencias / riesgos:** La mezcla necesita memoria auxiliar O(n); las conclusiones de tiempo solo son válidas para el equipo y rango medido.
