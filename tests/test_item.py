"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

test_item1 = Item('Iphone', 3000.00, 5)
test_item2 = Item('MacBook', '15000', '2')


def test_calculate_total_price():
    assert test_item1.calculate_total_price() == 15000.0
    # assert test_item2.calculate_total_price() == 0

    with pytest.raises(TypeError):
        test_item2.calculate_total_price()


def test_apply_discount():
    assert test_item1.apply_discount() is None
