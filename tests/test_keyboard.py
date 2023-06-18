from src.keyboard import KeyBoard
import pytest

kb = KeyBoard('Dark Project KD87A', 9600, 5)

def test_init():
    assert kb.name == 'Dark Project KD87A'
    assert kb.price == 9600
    assert kb.language == 'EN'
    assert kb.quantity == 5
def test_change_lang():
    assert kb.language == 'EN'
    kb.change_lang()
    assert kb.language == 'RU'
    kb.change_lang().change_lang()
    assert kb.language == 'RU'

    with pytest.raises(ValueError, match="AttributeError: property 'language' of 'KeyBoard' object has no setter"):
        kb.language = 'FR'
        kb.language = 'CH'
