// 曜日を定義
const weekDay = ["日", "月", "火", "水", "木", "金", "土"];

// 現在時刻を取得
const now = new Date();

// 年月日、その日の曜日をそれぞれ取得
const nowYear = now.getFullYear();
let month = now.getMonth();

// -mのコマンドオプションの処理
mOfIndex = process.argv.indexOf("-m");

// -mがコマンドオプションに含まれている場合
if (mOfIndex !== -1) {
  const choicedMonth = process.argv.at(mOfIndex + 1);

  // -mに続く引数がない時
  if (choicedMonth === undefined) {
    // 何もしない処理
  } else if (Number(choicedMonth) >= 1 && Number(choicedMonth) <= 12) {
    // 引数が存在する場合
    // 引数が1以上12以下の時、monthを更新
    month = Number(choicedMonth) - 1;
  } else {
    // 引数が不正の値のとき、エラーメッセージを出力
    console.log("月の値が不正です。\n正しい月を入力してください。");
    process.exit(1);
  }
}

// カレンダーの西暦と月を出力
const calendarHeader = `${month + 1}月 ${nowYear}`;
const spacing = "      ";
console.log(spacing + calendarHeader + spacing);

// 曜日を出力
console.log(weekDay.join(" "));

// 日付を出力

// 月末の日付を取得
const totalDays = new Date(nowYear, month + 1, 0).getDate();

// 1日から月末までの数字が入った配列を定義
const days = [];
for (let i = 1; i <= totalDays; i++) {
  days.push(String(i).padStart(2, " "));
}

// 曜日のインデックスと1日の曜日を合わせるため空白を追加
const firstDayOfTheWeek = new Date(nowYear, month, 1).getDay();
for (let i = 0; i < firstDayOfTheWeek; i++) {
  days.unshift("  ");
}

// 日付を出力
for (let i = 0; i < days.length; i += 7) {
  const weekDays = days.slice(i, i + 7);
  console.log(weekDays.join(" "));
}
