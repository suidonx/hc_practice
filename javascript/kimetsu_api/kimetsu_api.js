const BASE_URL = "https://ihatov08.github.io";

// 鬼滅キャラクターをfetchする
async function fetchKimetsuCharacters(fileName) {
  const response = await fetch(BASE_URL + `/kimetsu_api/api/${fileName}.json`);
  return await response.json();
}

// 鬼滅キャラクターをDOM要素に追加する
async function appendKimetsuCharacters(fileName) {
  const tableEl = document.querySelector("table");

  // すでに追加したtr要素がある場合は削除して初期化
  const trEls = document.querySelectorAll(".data");
  for (let trEl of trEls) {
    trEl.remove();
  }

  const characters = await fetchKimetsuCharacters(fileName);

  // 取得したデータを使って、tr要素を1つずつ作成して追加
  for (character of characters) {
    const trEl = document.createElement("tr");
    trEl.className = "data";

    const nameTdEl = document.createElement("td");
    const ImageTdEl = document.createElement("td");
    const CategoryTdEl = document.createElement("td");

    nameTdEl.innerText = character.name;

    const imgEl = document.createElement("img");
    imgEl.src = BASE_URL + `${character.image}`;
    ImageTdEl.appendChild(imgEl);

    CategoryTdEl.innerText = character.category;

    trEl.appendChild(nameTdEl);
    trEl.appendChild(ImageTdEl);
    trEl.appendChild(CategoryTdEl);

    tableEl.appendChild(trEl);
  }
}

// ローディング画面を表示する
function startLoading() {
  let isLoading = document.getElementById("loading");
  const tableEl = document.querySelector("table");
  isLoading.hidden = false;
  tableEl.hidden = true;
}

// ローディング画面を止める
function stopLoading() {
  let isLoading = document.getElementById("loading");
  const tableEl = document.querySelector("table");
  setTimeout(() => {
    isLoading.hidden = true;
    tableEl.hidden = false;
  }, 2000);
}

// ラジオボタンの処理
const allCharactersEl = document.getElementById("all");
const kisatsutaiEl = document.getElementById("kisatsutai");
const hashiraEl = document.getElementById("hashira");
const oniEl = document.getElementById("oni");

allCharactersEl.addEventListener("click", () => {
  startLoading();
  appendKimetsuCharacters(allCharactersEl.id);
  stopLoading();
});

kisatsutaiEl.addEventListener("click", () => {
  startLoading();
  (appendKimetsuCharacters(kisatsutaiEl.id), stopLoading());
  stopLoading();
});

hashiraEl.addEventListener("click", () => {
  startLoading();
  appendKimetsuCharacters(hashiraEl.id);
  stopLoading();
});

oniEl.addEventListener("click", () => {
  startLoading();
  appendKimetsuCharacters(oniEl.id);
  stopLoading();
});

// デフォルトで全キャラクター一覧を表示
appendKimetsuCharacters(allCharactersEl.id);
