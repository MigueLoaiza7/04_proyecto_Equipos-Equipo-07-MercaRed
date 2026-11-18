# Registro de decisiones técnicas (ADR breve)

Cada decisión importante se registra aquí y se enlaza desde el issue o PR correspondiente.

## D-001 — Estrategia A como línea base
- **Fecha:** 2026-11-18 · **Autor(es):** Equipo 7 / Copilot SDK · **Issue/PR:** por crear
- **Contexto:** La rama Estrategia-A y la tabla del README identifican A como la situación inicial: inserción más búsqueda lineal.
- **Opciones consideradas:** 1) Reusar `linea_base.py`; 2) crear un módulo independiente `estrategia_a.py`.
- **Decisión:** Crear `src/estrategia_a.py` como envoltura pública de las funciones verificadas de la línea base.
- **Justificación (incluya evidencia o principio físico):** Preserva el contrato `preparar(n)`/`ejecutar(datos)`, evita dividir la implementación entre el experimento y las pruebas y hace trazable a A.
- **Consecuencias / riesgos:** A conserva complejidad cuadrática de ordenamiento y lineal por consulta. No se promete escalamiento mayor que el rango medido.

## D-002 — Alcance inicial de medición
- **Fecha:** 2026-11-18 · **Autor(es):** Equipo 7 / Copilot SDK · **Issue/PR:** por crear
- **Contexto:** Los tamaños de la plantilla debían ejecutarse y la línea base crece rápido.
- **Opciones consideradas:** 1) incluir hasta 500 000; 2) mantener 1 000–4 000 y declararlo preliminar.
- **Decisión:** Mantener 1 000, 2 000 y 4 000 para el experimento formal inicial.
- **Justificación:** Permite cinco o diez repeticiones, calentamiento y medición de memoria sin exceder el propósito de una prueba reproducible.
- **Consecuencias / riesgos:** Los resultados no extrapolan directamente a 500 000; deben presentarse como evidencia dentro del rango medido.
- **Fecha:** · **Autor(es):** · **Issue/PR:** #
- **Contexto:** ¿qué problema o pregunta motivó la decisión?
- **Opciones consideradas:** 1) … 2) … 3) …
- **Decisión:**
- **Justificación (incluya evidencia o principio físico):**
- **Consecuencias / riesgos:**
