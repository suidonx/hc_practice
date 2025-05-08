# 購入処理をした際に、チャージ金額が足りない、在庫が足りない場合に例外を送出させる
class PurchaseException(Exception):
    def __str__(self):
        return "チャージ残高が足りません、もしくは在庫がありません。"