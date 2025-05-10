from pikachu import Pikachu

if __name__ == "__main__":
    pika = Pikachu("ピカチュウ", "でんき", "", 10)
    pika.name = "テキセツ"
    print(pika.name)  # テキセツ

    pika.name = "うんこ"  # 不適切な名前です、と表示される
    print(pika.name)  # テキセツ　のまま
