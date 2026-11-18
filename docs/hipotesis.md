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
| H1 | Si se duplica n en la Estrategia A, entonces el tiempo de pared aumentará aproximadamente según una tendencia cuadrática, porque ordenamiento por inserción realiza comparaciones proporcionales a n² para datos aleatorios; manteniendo semilla, equipo y consultas | n | tiempo (s) | Entre 3× y 5× al duplicar n | Comparaciones de inserción y traslados | Pendiente log-log de tiempo próxima a 2 y/o razón distinta de 2 se refuta |
| H2 | Si se duplica n, entonces el pico de memoria crecerá aproximadamente de forma lineal, porque el catálogo y las consultas crecen con n y se usa una copia para ordenar | n | pico Python (MiB) | Aproximadamente 2× al duplicar n | Capacidad del catálogo y copia de Python | Razón muy distinta de 2 fuera de la dispersión experimental |
| H3 | Si se compara el tiempo con el tamaño medido, entonces el uso de CPU (%) no puede interpretarse como consumo eléctrico, porque el arnés usa una fracción de tiempo de CPU sin RAPL o vatímetro | estrategia/tamaño | uso CPU (%) y energía | Sin estimación ni afirmación de ahorro energético | Variación de carga del núcleo | Cualquier afirmación de ahorro energético requeriría medición eléctrica separada |

## Lista de verificación
- [ ] Tiene dirección (aumenta/disminuye) y una magnitud aproximada.
- [ ] La VD es medible con las herramientas disponibles en el laboratorio.
- [ ] Indica qué resultado la **refutaría**.
- [ ] Explica el mecanismo con al menos una magnitud física y su unidad SI.
- [ ] No afirma ahorro de energía si no se va a medir energía.
