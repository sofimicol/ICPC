# Problema F — Frío en la playa

Un grupo de amigos, ya retirados de la programación competitiva, decidieron improvisadamente tomarse una semana de vacaciones en la ciudad de la costa Mar de AJI.

Como no miraron el pronóstico, al llegar se encontraron días nublados y ventosos. Pero las condiciones meteorológicas no iban a arruinarles sus vacaciones.

Para divertirse en la playa, decidieron organizar un torneo de tejo entre dos equipos, llamados **A** (equipo azul) y **R** (equipo rojo).

El tejo se juega en una cancha de forma rectangular delimitada sobre la arena que tiene **W** centímetros de ancho y **L** centímetros de largo. Las esquinas de esta cancha tienen coordenadas `(0,0)`, `(W,0)`, `(0,L)` y `(W,L)`.

Inicialmente hay un tejín en la posición `(Tx,Ty)`.

Luego, cada equipo realiza **N** lanzamientos de discos (llamados tejos) buscando quedar lo más cercano al tejín posible (inclusive pudiendo quedar en la misma posición del tejín, situado por encima de él).

Al finalizar los **N** lanzamientos, el equipo que haya lanzado el tejo que quedó más cerca del tejín es el equipo ganador.

Además, el equipo ganador recibe un punto por cada tejo que esté más cerca del tejín que el tejo del equipo rival que se encuentra más cercano al tejín.

La distancia de un tejo al tejín se mide como la distancia euclídea del centro del tejín al centro del tejo.

Además de los lanzamientos de los equipos, se conoce la posición del centro del tejín.

Se asegura que todos los lanzamientos se ubican dentro de los límites de la cancha (o sobre la línea) y que en la entrada no hay dos tejos a la misma distancia del tejín.

Se te pide calcular qué equipo resultó ganador y cuántos puntos obtuvo.

## Entrada

Una primera línea con un entero:

- `N` (`1 ≤ N ≤ 1000`), la cantidad de lanzamientos que realizó cada equipo.

Luego, una segunda línea con cuatro enteros `W`, `L`, `Tx` y `Ty`.

Los primeros dos corresponden a las dimensiones en ancho y largo de la cancha:

- `1 ≤ W ≤ 10^4`
- `1 ≤ L ≤ 10^4`

Los últimos dos corresponden a la ubicación del tejín:

- `0 ≤ Tx ≤ W`
- `0 ≤ Ty ≤ L`

Luego `N` líneas, cada una con dos enteros que describen cada lanzamiento del equipo **A**.

La `i`-ésima línea contiene dos enteros `Xi`, `Yi`, donde:

- `Xi` indica la ubicación en ancho del `i`-ésimo lanzamiento.
- `Yi` denota la ubicación en largo del `i`-ésimo lanzamiento.

Se cumple que:

- `0 ≤ Xi ≤ W`
- `0 ≤ Yi ≤ L`

Finalmente siguen `N` líneas que describen de la misma forma los lanzamientos del equipo **R**.

## Salida

Una única línea con dos valores separados por un espacio.

El primero debe ser `A` o `R`, según qué equipo resultó ganador, y el segundo la cantidad de puntos que recibe dicho equipo al finalizar todos los lanzamientos.

## Ejemplos
<img width="906" height="236" alt="image" src="https://github.com/user-attachments/assets/add12d21-3e7d-404c-bbba-34160068a33d" />
<img width="922" height="862" alt="image" src="https://github.com/user-attachments/assets/57bb349d-7091-438a-a0ae-bb04e7dba036" />


## Explicación del primer ejemplo

La imagen corresponde al primer ejemplo.

Cada equipo realizó dos lanzamientos.

Los tejos azules, con un triángulo en su interior, corresponden al equipo **A** en las posiciones `(1,3)` y `(4,2)`.

Los tejos rojos, con un cuadrado en su interior, corresponden al equipo **R**, en las posiciones `(3,2)` y `(5,5)`.

La cancha mide `5` centímetros de ancho y largo.

El tejín, con una estrella en su interior, se encuentra en la posición `(1,2)`.

Las distancias de los lanzamientos al tejín son `1`, `3`, `2` y `5`, donde los primeros dos lanzamientos corresponden al equipo **A** y los últimos dos al equipo **R**.

El equipo **A** resulta ganador y recibe solamente `1` punto, que corresponde al tejo que está a `1` centímetro de distancia del tejín.

---

**Torneo Argentino de Programación 2023**
