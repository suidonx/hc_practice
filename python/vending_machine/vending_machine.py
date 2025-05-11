from exceptions import PurchaseException
from juice import Juice


class VendingMachine:
    def __init__(self):
        # 自動販売機の在庫を定義
        self._stock = []
        for i in range(5):
            self._stock.append(Juice("Pepsi", 150))
            self._stock.append(Juice("Monster", 230))
            self._stock.append(Juice("Ilohas", 120))
        # 自動販売機の売り上げを定義
        self._sales = 0

    # ゲッターを使って自動販売機の在庫を取得できる
    @property
    def stock(self):
        return self._stock

    # 自動販売機の在庫のセッター
    @stock.setter
    def stock(self, stock):
        self._stock = stock

    # ゲッターを使って現在の売り上げ金額を取得できる
    @property
    def sales(self):
        return self._sales

    # 売り上げのセッター
    @sales.setter
    def sales(self, sales):
        self._sales = sales

    # 自動販売機で任意のジュースは購入できるのかどうか取得する
    def can_purchasable_juice(self, juice_name):
        for juice in self.stock:
            if juice.name == juice_name:
                return True
        return False

    # 購入可能なドリンクのリストを取得
    def get_purchasable_drinks(self):
        purchasble_drinks = []
        for juice in self.stock:
            if juice.name not in purchasble_drinks:
                purchasble_drinks.append(juice.name)
        return purchasble_drinks

    # 自動販売機に在庫を補充する
    def add_stock(self, juice):
        self.stock.append(juice)

    # 購入処理
    # suicaと購入したいジュースの名前を引数に入れる
    def purchase(self, suica, juice_name):
        for i, juice in enumerate(self.stock):
            # 購入するジュースが在庫に無い、もしくはチャージ残高が足りない場合、例外を出す
            if not (
                self.can_purchasable_juice(juice_name) and suica.balance >= juice.price
            ):
                raise PurchaseException
            # 購入するジュースの名前とjuice.nameが一致して無ければcontinue
            if juice_name != juice.name:
                continue
            # 在庫から買った本数分減らす
            self.stock.pop(i)
            # 売り上げ金額を増やす
            self.sales += juice.price
            # Suicaのチャージ残高を減らす
            suica.balance -= juice.price
            break
