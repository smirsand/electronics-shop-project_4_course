from src.item import Item


class KeyboardMixin:

    def __init__(self):
        self._language = 'EN'

    @property
    def language(self):
        return self._language

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'
        return self


class Keyboard(Item, KeyboardMixin):
    """
    Класс для представления клавиатуры в магазине.
    """

    pass
