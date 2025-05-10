class Pokemon:
    name = "リザードン"
    type1 = "ほのお"
    type2 = "ひこう"
    hp = 100
    mp = 10  # 追加

    def attack(self):
        print(f"{Pokemon.name} のこうげき！")
