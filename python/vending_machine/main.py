from exceptions import PurchaseException
from juice import Juice
from suica import Suica
from vending_machine import VendingMachine


# 簡易的な動作確認
if __name__ == "__main__":
    # step1: suica
    print("---step1---")
    my_suica = Suica()
    # 100円以上の任意の金額をチャージできる
    my_suica.charge_balance(100)
    my_suica.charge_balance(10000)
    # 100円未満をチャージすると例外発生
    try:
        my_suica.charge_balance(99)
    except ValueError as e:
        print(e)
    print(f"現在のチャージ残高 : {my_suica.balance}")

    # step2 juice
    print("---step2---")
    vend_1 = VendingMachine()
    black = Juice("Black", 100)
    # 自動販売機の在庫を取得
    current_stock = vend_1.stock

    # step3-4
    print("---step3,4---")
    # ペプシは買えるのか？
    print(f"ペプシは購入可能か？ : {vend_1.can_purchasable_juice("Pepsi")}")

    # ペプシ、モンスター、いろはすを1本ずつ購入
    vend_1.purchase(my_suica, "Pepsi")
    vend_1.purchase(my_suica, "Monster")
    vend_1.purchase(my_suica, "Ilohas")

    # それぞれ購入後の現在の打ち上げ
    print(f"購入後の売り上げ : {vend_1.sales}")

    # ペプシを10本購入すると途中で在庫がなくなるので例外が発生
    for i in range(10):
        try:
            vend_1.purchase(my_suica, "Pepsi")
        except PurchaseException as e:
            print(e)
            break

    # ペプシ4本購入後の自動販売機の現在の売り上げを出力
    print(f"購入後の売り上げ : {vend_1.sales}")

    # 購入可能なドリンクのリストを出力
    print(f"購入可能なドリンクのリスト : {vend_1.get_purchasable_drinks()}")

    # 自動販売機に在庫を補充する
    pepsi2 = Juice("Pepsi2", 10000)
    vend_1.add_stock(pepsi2)
    print(f"在庫補充後の購入可能なドリンクのリスト : {vend_1.get_purchasable_drinks()}")
