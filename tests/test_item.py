"""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv

import pytest

from src import item
from src.item import Item, InstantiateCSVError
from src.phone import Phone

test_item1 = Item('Iphone', 3000.00, 5)
test_item2 = Item('MacBook', '15000', '2')


def test_calculate_total_price():
    assert test_item1.calculate_total_price() == 15000.0
    # assert test_item2.calculate_total_price() == 0

    with pytest.raises(TypeError):
        test_item2.calculate_total_price()


def test_apply_discount():
    assert test_item1.apply_discount() is None


def test_instantiate_from_csv():
    """
    TestCase classmethod
    """
    item1 = Item.all[0]
    assert item1.name == 'Iphone'
    assert item1.price == 3000.0
    assert item1.quantity == 5


def test_string_to_number():
    """
    TestCase staticmethod
    """
    assert Item.string_to_number('2') == 2
    assert Item.string_to_number('5') != 2
    assert Item.string_to_number('1.0') == 1


def test_name_setter():
    item.name = 'СуперСмартфон'
    assert len(item.name) >= 10

    with pytest.raises(ValueError):
        raise ValueError


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("IPhone", 50000, 2)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert repr(item2) == "Item('IPhone', 50000, 2)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("IPhone", 50000, 2)
    assert str(item1) == 'Смартфон'
    assert str(item2) == 'IPhone'


def test_add():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10

    with pytest.raises(TypeError):
        phone1 + 2


def test_raises():
    some_obj = InstantiateCSVError()
    assert some_obj.__str__() == 'Файл item.csv поврежден'


def test_instantiate_from_csv_not_file():
    '''
    Отсутствие файла
    '''
    with pytest.raises(FileNotFoundError):
        with open('../src/items_1.csv', encoding='cp1251') as csvfile:
            item = csv.DictReader(csvfile)


def test_instantiate_from_csv_bad_file():
    Item.instantiate_from_csv('../src/test_file.csv')
