import random

# 'A', 'B', 'C', 'D', 'E', 'F'のリスト
groups = [chr(c) for c in range(ord('A'), ord('F')+1)]

def divide_groups(groups):
    # 6人のリストをランダムにシャッフルする
    random.shuffle(groups)

    # ランダムで0か1か決める
    pattern = random.randint(0, 1)

    # 1の場合、2人と4人に分ける
    if pattern:
        print(sorted(groups[:2]))
        print(sorted(groups[2:]))
    
    # 0の場合、3人と3人に分ける
    else:
        print(sorted(groups[:3]))
        print(sorted(groups[3:]))

if __name__ == '__main__':
    divide_groups(groups)