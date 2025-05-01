import datetime
import locale
import sys

# ロケールを日本語に設定
locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')


# -mで指定した月をreturnする
# -mで引数を指定しない場合は今月をreturnする
def get_month(argv):
    idx = find_dash_m(argv)
    # -mが存在しない、または-mのインデックスがリストの最後の要素の場合、今月をreturnする
    if idx is None or idx == len(argv)-1:
        return datetime.date.today().month
    # -mで指定された値が有効な値の場合、その月をreturnする
    if is_valid_dash_m(argv, idx):
        return int(argv[idx+1])


# -mで指定した値が文字列もしくは不正な月の場合はエラーメッセージを出力してプログラムを終了させる
# -mで指定した値が有効の場合はTrueを返す
def is_valid_dash_m(argv, idx):
    try:
        dash_m_value = int(argv[idx+1])
        if 1 <= dash_m_value <= 12:
            return True
        else:
            raise ValueError
    except ValueError:
        print(f'{argv[idx+1]} is neither a month number (1..12) nor a name')
        sys.exit(1)


# コマンドライン引数のリストの中から-mがあるインデックスを戻す
def find_dash_m(argv):
    if '-m' in argv:
        return argv.index('-m')
    else:
        return None


# コマンドライン引数のリストを受け取る
argv = sys.argv

# 西暦、月、曜日を定義
today = datetime.date.today()
year = today.year
month = get_month(argv)
weekdays = ['月', '火', '水', '木', '金', '土', '日']

# 指定月のdateインスタンスを生成
date = datetime.date(today.year, month, 1)

# 出力用にフォーマットする
formatted_date = date.strftime('%B %Y')
space_fill = 20
formatted_weekdays = ' '.join(weekdays)

# 月と西暦を中央寄せで表示
print(f'{formatted_date:^{space_fill}}')

# 曜日を月曜日から順に表示
print(formatted_weekdays)

# 月の最終日は何日か計算
if month == 12:
    next_month = datetime.date(year+1, 1, 1)
else:
    next_month = datetime.date(year, month%12+1, 1)
last_day = (next_month - date).days

# 指定した月の1日は何曜日か計算
weekday_of_first_day = date.weekday()

# 1日から31日までを表示
for i, v in enumerate(range(1,last_day+1)):
    # 1日目の曜日に合わせて空白を入れる
    if i == 0:
        print('   ' * weekday_of_first_day, end='')

    # 今日の日付をハイライトする
    if v == today.day:
        print('\033[48;2;204;204;204m'+f'{v:2d}'+'\033[0m', end='')
    else:
        print(f'{v:2d}', end='')

    # iが日曜日、vが最終日の場合、改行を入れる
    # そうでない場合、空白を入れる
    if i % 7 == (6 - weekday_of_first_day) or v == last_day:
        print('')
    else:
        print(' ', end='')
