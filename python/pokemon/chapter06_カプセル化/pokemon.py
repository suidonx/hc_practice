from abc import ABC, abstractmethod


class Pokemon(ABC):
    def __init__(self, name, type1, type2, hp):
        # 変数名に_をつけて隠蔽する
        self._name = name
        self._type1 = type1
        self._type2 = type2
        self._hp = hp

    @abstractmethod
    def attack(self): ...

    @property
    def name(self):
        return self._name

    # 例で紹介されているchangeNameメソッドに相当
    @name.setter
    def name(self, name):
        # 不適切な名前はエラー
        if name == "うんこ":
            print("不適切な名前です")
            return
        self._name = name
