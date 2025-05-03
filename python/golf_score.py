# ゴルフスコアの用語を定義
golf_scores = [
    'パー',
    'バーディ',
    'イーグル',
    'アルバトロス',
    'コンドル',
    'ボギー',
]
hole_in_one = 'ホールインワン'

# 各ホールの規定打数とプレイヤーの打数を標準入力でリストに受け取る
pars = list(map(int, input().split(',')))
strokes = list(map(int, input().split(',')))

# 各ホールのゴルフスコアを格納するリストを定義
result = []
for i in range(len(pars)):
    par = pars[i]
    stroke = strokes[i]
    score = par - stroke

    # プレイヤーの打数が1で規定打数が5ではないときホールインワンと出力
    if stroke == 1 and par != 5:
        result.append(hole_in_one)
    
    # ゴルフスコアがダブルボギー以上の場合はは接頭辞をつける
    elif score < -1:
        result.append(f'{-score}{golf_scores[-1]}')
    
    # ゴルフスコアリストのインデックスと(規定打数ープレイヤーの打数)が対応するので
    # そのまま出力
    else:
        result.append(golf_scores[score])

# 出力様式に合わせる
formatted_result = ','.join(result)

# 出力
print(formatted_result)