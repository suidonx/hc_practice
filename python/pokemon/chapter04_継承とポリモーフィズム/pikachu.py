from pokemon import Pokemon


class Pikachu(Pokemon):
    def __init__(self, name, type1, type2, hp):
        super().__init__(name, type1, type2, hp)

    def attack(self):
        super().attack()  # 親クラスのメソッド呼び出し
        print(f"{self.name} の10万ボルト！")
