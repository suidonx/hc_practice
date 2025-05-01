import random

# 'A', 'B', 'C', 'D', 'E', 'F'のリスト
groups = [chr(c) for c in range(ord('A'), ord('F')+1)]

def divide_groups(groups):
    # 6人のリストをランダムにシャッフルする
    random.shuffle(groups)

    # ランダムで2人と4人、3人と3人のどちらの人数で分けるか決める
    pattern = random.randint(2, 3)

    # それぞれの組のメンバーを出力する
    print(sorted(groups[:pattern]))
    print(sorted(groups[pattern:]))
    

if __name__ == '__main__':
    divide_groups(groups)