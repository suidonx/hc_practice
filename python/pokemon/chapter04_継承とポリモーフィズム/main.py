from pikachu import Pikachu

if __name__ == "__main__":
    pika = Pikachu("ピカチュウ", "でんき", "", 100)

    print(pika.name)  # ピカチュウ

    # ピカチュウの こうげき！
    # ピカチュウ の10万ボルト！　が順番に表示される
    pika.attack()
