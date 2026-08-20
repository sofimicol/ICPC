# Problema A — Alfajores

Seba es el gerente del Taller de Avioncitos de Papel (TAP), una empresa muy grande dedicada al arte de la papiroflexia. El TAP cuenta con un edificio muy grande que posee `M` oficinas. En la `i`-ésima oficina trabajan `E_i` empleados.

Debido a la gran demanda de su producto, Seba viaja constantemente. Al regresar de sus viajes, tiene por costumbre traer una gran caja de alfajores para compartir con sus empleados.

Para repartirlos, visita cada una de las `M` oficinas de la empresa en orden, desde la `1` hasta la `M`.

Cuando llega a la `i`-ésima oficina, reparte tantos alfajores como le sea posible en partes iguales entre los `E_i` empleados de la oficina. Luego de repartirlos, toma la caja con los alfajores restantes y pasa con ellos a la siguiente oficina.

Una vez que ha visitado todas las oficinas, se sienta en su escritorio y disfruta de los alfajores restantes.

Seba tiene miedo de estar excediéndose con los dulces, y por eso necesita saber cuántos alfajores ha consumido. El problema es que no lleva el registro de la cantidad que quedó en la caja luego de la repartición correspondiente a cada viaje. Por suerte, cuenta con los `N` tickets correspondientes a las compras de alfajores, y como sabe cuántas personas trabajan en cada oficina, está seguro de que podrás calcular dichas cantidades por él.

## Entrada

Una primera línea con dos enteros `N` y `M` (`1 ≤ N, M ≤ 10^5`), que representan la cantidad de viajes que hizo Seba y la cantidad de oficinas del TAP.

Una segunda línea con `N` enteros `A_1, A_2, ..., A_N` (`1 ≤ A_i ≤ 10^9`), donde `A_i` es la cantidad de alfajores que compró en el `i`-ésimo viaje.

Finalmente, una tercera línea con `M` enteros `E_1, E_2, ..., E_M` (`1 ≤ E_i ≤ 10^9`), donde `E_i` es la cantidad de personas que trabajan en la `i`-ésima oficina.

## Salida

Una única línea con `N` enteros, las cantidades de alfajores que quedaron en la caja luego de la repartición correspondiente a cada uno de los viajes de Seba.

## Ejemplo de entrada 1

```text
3 3
140 79 5
90 42 5

Ejemplos
Ejemplo	Entrada	Salida
1	3 3<br>140 79 5<br>90 42 5	3 2 0
2	10 8<br>120 456 7458 84 123 84 213 185 987 654<br>97 73 61 41 52 23 11 7	0 0 2 0 3 0 1 4 6 0
