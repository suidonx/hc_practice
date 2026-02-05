const inputToDoItem = document.getElementById("input-todo");
const createButton = document.getElementById("add-todo");
const ul = document.querySelector("ul");

const allTask = document.getElementById("all-task");
const doneTask = document.getElementById("done-task");
const todoTask = document.getElementById("todo-task");

// 集計用変数
let allTaskCount = 0;
let doneCount = 0;
let todoCount = 0;

// 新規todoを追加する
createButton.addEventListener("click", (event) => {
  // 前後の空白を除く
  let todoItemName = inputToDoItem.value.trim();

  // 入力フォームに文字がない場合、処理をしない
  if (!todoItemName) {
    return;
  }

  // li要素を作成
  const li = document.createElement("li");

  // li要素にtodo itemに必要な各要素を追加
  // checkboxを定義
  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";

  // checkboxがclickされた場合に、todo itemのカウントを更新する
  checkbox.addEventListener("click", (event) => {
    if (checkbox.checked) {
      doneCount++;
      todoCount--;
      doneTask.innerText = `完了済み：${doneCount}`;
      todoTask.innerText = `未完了：${todoCount}`;
    } else if (!checkbox.checked) {
      doneCount--;
      todoCount++;
      doneTask.innerText = `完了済み：${doneCount}`;
      todoTask.innerText = `未完了：${todoCount}`;
    }
  });

  // 編集ボタンを定義
  const updateButton = document.createElement("button");
  updateButton.innerText = "編集";

  // 編集ボタンがclickされた場合、入力フォームに変わりタスク名を編集できる
  updateButton.addEventListener("click", (event) => {
    // li要素を編集用のフォームにする
    li.innerHTML = "";
    const inputText = document.createElement("input");
    inputText.type = "text";
    li.appendChild(inputText);
    inputText.value = todoItemName;

    // 保存ボタンを追加
    const saveButton = document.createElement("button");
    saveButton.innerText = "保存";
    li.appendChild(saveButton);

    // 保存ボタンを押すと、編集した名前に更新できる
    saveButton.addEventListener("click", (event) => {
      const newTodoItemName = inputText.value;

      // li要素を元の表示に戻す処理
      li.innerHTML = "";

      // todo itemの名前を更新
      todoItemName = newTodoItemName;

      // li要素に各要素を追加
      li.appendChild(checkbox);
      li.appendChild(document.createTextNode(newTodoItemName));
      li.appendChild(updateButton);
      li.appendChild(deleteButton);
    });
  });

  // 削除ボタンを追加
  const deleteButton = document.createElement("button");
  deleteButton.innerText = "削除";

  // 削除処理
  deleteButton.addEventListener("click", (event) => {
    if (confirm("本当に削除してもよろしいですか？")) {
      // カウントを更新
      allTaskCount--;
      allTask.innerText = `全てのタスク：${allTaskCount}`;

      if (checkbox.checked) {
        doneCount--;
        doneTask.innerText = `完了済み：${doneCount}`;
      } else {
        todoCount--;
        todoTask.innerText = `未完了：${todoCount}`;
      }

      // li要素の削除
      li.remove();
    }
  });

  // li要素に追加
  li.appendChild(checkbox);
  li.appendChild(document.createTextNode(todoItemName));
  li.appendChild(updateButton);
  li.appendChild(deleteButton);

  // HTMLのul要素に追加
  ul.appendChild(li);

  // タスク数を+1して表示を更新
  allTaskCount++;
  todoCount++;
  allTask.innerText = `全てのタスク：${allTaskCount}`;
  todoTask.innerText = `未完了：${todoCount}`;

  // 入力欄を空文字にする
  inputToDoItem.value = "";
});
