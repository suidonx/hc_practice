from exceptions import PurchaseException
from juice import Juice


class VendingMachine:
    def __init__(self):
        # 自動販売機の在庫を定義
        self._stock = [
            [Juice("Pepsi", 150), 5],
            [Juice("Monster", 230), 5],
            [Juice("Ilohas", 120), 5],
        ]
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

    # ペプシが在庫に存在し、在庫が0より大きければ購入できる
    def purchasable_pepsi(self):
        for stock in self.stock:
            if stock[0].name == "Pepsi" and stock[1] > 0:
                print("ペプシが購入可能です")
                return
        print("ペプシは購入できません")

    # 購入可能なドリンクのリストを取得
    def get_purchasable_drinks(self):
        purchasble_drinks = []
        for stock in self.stock:
            if stock[1] > 0:
                purchasble_drinks.append([stock[0].name, stock[1]])
        return purchasble_drinks

    # 自動販売機に在庫を補充する
    def add_stock(self, juice, num_of_bottles):
        self.stock.append([juice, num_of_bottles])

    # 購入処理
    # suicaと購入したいジュースの名前を引数に入れる
    def purchase(self, suica, juice_name, num):
        for stock in self.stock:
            # stockのリストが購入するジュース名と異なる場合はcontinueする
            if stock[0].name != juice_name:
                continue
            if num < 0:
                raise ValueError("0以上の整数を入力してください")

            # ジュースの在庫があり、かつSuicaのチャージ金額がジュース値段以上であれば購入処理をする
            if stock[1] >= num and suica.balance >= stock[0].price:
                # 在庫から買った本数分減らす
                stock[1] -= num
                # 売り上げ金額を増やす
                self.sales += stock[0].price * num
                # Suicaのチャージ残高を減らす
                suica.balance -= stock[0].price
                break
            else:
                # 購入できない場合は例外を発生
                raise PurchaseException
