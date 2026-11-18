# Plantilla de hipótesis

Una hipótesis verificable **predice un resultado medible** y **puede resultar falsa**.

## Estructura
> **Si** _(cambio en la variable independiente)_, **entonces** _(variable dependiente, con unidad)_
> **aumentará / disminuirá** aproximadamente _(magnitud o factor)_, **porque** _(mecanismo físico/computacional)_,
> **manteniendo constantes** _(variables controladas)_.

## Ejemplo (problema neutro de la demostración, NO de un equipo)
> **Si** se reemplaza la lista intermedia por un generador al sumar n cuadrados, **entonces** el pico de memoria
> (MiB) **disminuirá** en más de un 90 % para n = 10⁶ y el tiempo (s) variará menos de un 20 %, **porque** el
> generador no almacena los n valores (memoria constante) pero realiza el mismo número de operaciones,
> **manteniendo** el mismo equipo, versión de Python y n.

## Hipótesis del equipo
| Id | Hipótesis completa | VI | VD (unidad) | Predicción cuantitativa | Mecanismo físico | ¿Cómo la refutaríamos? |
|---|---|---|---|---|---|---|
| H1 | Si se usa Estrategia C en lugar de A con el mismo n, entonces el tiempo de pared disminuirá, porque C construye un diccionario una vez y resuelve consultas por clave en lugar de ordenar por inserción y buscar linealmente; manteniendo datos, equipo y semilla | estrategia y n | tiempo (s) | Menor tiempo para C en el rango medido | Operaciones por clave y número de comparaciones | Si C no es sistemáticamente más rápida por la dispersión observada, la hipótesis se refuta |
| H2 | Si se duplica n en Estrategia C, entonces el tiempo crecerá aproximadamente de forma lineal, porque construir el índice recorre una vez el catálogo y las consultas se acceden por clave | n | tiempo (s) | Entre 1.5× y 3× al duplicar n | Recorrido lineal del catálogo | Pendiente log-log muy distinta de 1 dentro del rango medido |
| H3 | Si se usa Estrategia C, entonces el pico de memoria Python puede ser mayor que en A por almacenar el diccionario adicional | estrategia y n | pico Python (MiB) | C usa memoria adicional proporcional a n | Una clave y referencia por producto en el índice | Si no se observa crecimiento aproximadamente lineal o C no usa más memoria en el rango medido |

## Lista de verificación
- [ ] Tiene dirección (aumenta/disminuye) y una magnitud aproximada.
- [ ] La VD es medible con las herramientas disponibles en el laboratorio.
- [ ] Indica qué resultado la **refutaría**.
- [ ] Explica el mecanismo con al menos una magnitud física y su unidad SI.
- [ ] No afirma ahorro de energía si no se va a medir energía.
