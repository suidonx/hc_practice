from pokemon import Pokemon


def create_pokemon_100():
    pokemons = []
    for i in range(100):
        pokemons.append(Pokemon())
    return pokemons


if __name__ == "__main__":
    poke = Pokemon()

    print(poke.name)  # リザードン
    print(poke.type1)  # ほのお
    poke.attack()  # リザードン のこうげき！

    pokemons = create_pokemon_100()  # ポケモンのインスタンスを100匹分作る
    print(pokemons[0].name)  # 1匹目のポケモンの名前
    print(pokemons[9].type1)  # 10匹目のポケモンのタイプ1
    pokemons[99].attack()  # 100匹目のポケモンの攻撃

    print(poke.mp)  # 10
