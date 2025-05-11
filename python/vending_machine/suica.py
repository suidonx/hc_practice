class Suica:
    # 預かり金500円がデフォルトでチャージ
    def __init__(self):
        self._balance = 500

    # 現在のチャージ残高を取得するゲッター
    @property
    def balance(self):
        return self._balance

    # 残高のセッターを定義
    @balance.setter
    def balance(self, balance):
        self._balance = balance

    def charge_balance(self, amount):
        # 100円未満の金額をチャージしようとすると例外が発生
        if amount < 100:
            raise ValueError("100円未満の金額はチャージできません")
        # 100円以上であれば現在の残高にチャージする
        else:
            self._balance += amount
