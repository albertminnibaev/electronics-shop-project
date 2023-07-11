"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.phone import Phone
from src.item import Item, InstantiateCSVError


@pytest.fixture
def item_test():
    return Item("Ноутбук", 50000, 5)


@pytest.fixture
def phone_test():
    return Phone("Самсунг", 50000, 5, 2)


def test_item_init(item_test):
    assert item_test.name == "Ноутбук"
    assert item_test.price == 50000
    assert item_test.quantity == 5


def test_calculate_total_price(item_test):
    assert item_test.calculate_total_price() == 250000


def test_apply_discount(item_test):
    Item.pay_rate = 0.5
    item_test.apply_discount()
    assert item_test.price == 25000


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert Item.all[5].name == "Кабель"
    assert Item.all[5].price == 10.0
    assert Item.all[5].quantity == 5


def test_string_to_number():
    assert Item.string_to_number('7.0') == 7


def test_name():
    Item.all[6].name = "ИгроваяМышка"
    assert Item.all[6].name == "ИгроваяМыш"
    Item.all[6].name = "ИгроваяМ"
    assert Item.all[6].name == "ИгроваяМ"


def test___repr__(item_test):
    assert repr(item_test) == "Item('Ноутбук', 50000, 5)"


def test___str__(item_test):
    assert str(item_test) == 'Ноутбук'


def test___add__(item_test, phone_test):
    assert item_test + phone_test == 10


def test_error():
    with pytest.raises(FileNotFoundError):
        Item.checking_file_items()
    with pytest.raises(InstantiateCSVError):
        Item.checking_file_items()