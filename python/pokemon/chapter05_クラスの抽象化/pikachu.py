from pokemon import Pokemon


class Pikachu(Pokemon):
    # initを定義
    def __init__(self, name, type1, type2, hp):
        self._name = name
        self._type1 = type1
        self._type2 = type2
        self._hp = hp

    # attackをオーバーライド
    def attack(self):
        super().attack()
        print(f"{self.name} の10万ボルト！")

    # 以下、propertyとsetterをオーバーライド
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def type1(self):
        return self._type1

    @type1.setter
    def type1(self, type1):
        self._type1 = type1

    @property
    def type2(self):
        return self._type2

    @type2.setter
    def type2(self, type2):
        self._type2 = type2

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp
