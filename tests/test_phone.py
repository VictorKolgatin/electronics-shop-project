import pytest

from src.phone import Phone


def test_number_of_sim():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.number_of_sim == 2

    with pytest.raises(ValueError, match='Количество физических SIM-карт должно быть целым числом больше нуля.'):
        phone1.number_of_sim = 0
        phone1.number_of_sim = 1.0


