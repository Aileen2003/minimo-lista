from typing import Iterable, Union

Number = Union[int, float]


def minimo(lista: Iterable[Number]) -> Number:
    """
    Devuelve el valor mínimo de una lista/iterable de números.

    Reglas:
    - Si 'lista' es None, lanza TypeError.
    - Si la lista está vacía, lanza ValueError.
    - Si algún elemento no es int o float, lanza TypeError.

    Args:
        lista: Iterable de números (int o float).

    Returns:
        El número mínimo.

    Raises:
        TypeError: Si lista es None o contiene elementos no numéricos.
        ValueError: Si el iterable está vacío.
    """
    if lista is None:
        raise TypeError("La lista no puede ser None.")

    datos = list(lista)

    if len(datos) == 0:
        raise ValueError("La lista no puede estar vacía.")

    for x in datos:
        if not isinstance(x, (int, float)):
            raise TypeError(f"Elemento no numérico detectado: {x!r}")

    min_val = datos[0]
    for x in datos[1:]:
        if x < min_val:
            min_val = x

    return min_val
