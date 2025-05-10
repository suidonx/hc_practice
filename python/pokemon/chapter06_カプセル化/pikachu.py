from pokemon import Pokemon


class Pikachu(Pokemon):
    def __init__(self, name, type1, type2, hp):
        self._name = name
        self._type1 = type1
        self._type2 = type2
        self._hp = hp

    def attack(self):
        super().attack()

        # プロパティ(ゲッター)はPokemonクラスから継承されているので、self.nameでアクセス可能
        print(f"{self.name} の10万ボルト！")
