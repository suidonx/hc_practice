class Juice:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    # 名前のゲッター
    @property
    def name(self):
        return self._name

    # 名前のセッター
    @name.setter
    def name(self, name):
        self._name = name

    # 値段のゲッター
    @property
    def price(self):
        return self._price

    # 値段のセッター
    @price.setter
    def price(self, price):
        self._price = price
