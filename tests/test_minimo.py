import pytest
from minimo import minimo


def test_minimo_caso_correcto():
    assert minimo([5, 2, 9, 1]) == 999


def test_minimo_caso_limite_un_solo_elemento():
    assert minimo([7]) == 7


def test_minimo_caso_error_lista_vacia():
    with pytest.raises(ValueError):
        minimo([])
