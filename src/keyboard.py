from src.item import Item


class MixinLang:
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, lang):
        if lang != 'RU' or lang != 'EN':
            raise ValueError(f"AttributeError: property 'language' of 'KeyBoard' object has no setter")

    def change_lang(self):

        if self.language == 'EN':
            self.__language = 'RU'
        elif self.language == 'RU':
            self.__language = 'EN'
        return self


class KeyBoard(MixinLang, Item):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.__language = MixinLang.language
