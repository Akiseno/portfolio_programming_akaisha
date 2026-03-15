let counter = 0;
let allTask = [];
function addTask() {
  counter++;
  let input = document.getElementById("taskInput");
  let taskText = input.value;
  if (taskText.trim() === "") {
    alert("please type a task first");
    return;
  }
  let newItem = document.createElement("li");
  newItem.innerHTML = taskText;
  let list = document.getElementById("tasklist");
  list.appendChild(newItem);
  allTask.push(taskText);
  console.log(newItem);
  saveToLocalStorage();
  let counterText = document.getElementById("counter");
  counterText.innerHTML = counter;

  input.value = "";
}
document
  .getElementById("taskInput")
  .addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
      addTask();
    }
  });
function saveToLocalStorage() {
  let stringData = JSON.stringify(allTask);
  localStorage.setItem("myToDoList", stringData);
  console.log("data save to memory");
}
function loadFromLocalStorage() {
    let data = localStorage.getItem("myToDoList");
    if (data !== null) {
      allTask = JSON.parse(data);          // ["task1", "task2", ...]
      let list = document.getElementById("tasklist");
      list.innerHTML = "";                 // clear old list
  
      allTask.forEach(function (taskText) {
        let li = document.createElement("li");
        li.textContent = taskText;
        list.appendChild(li);
      });
    }
    console.log("data loaded");
  }
  function clearAllTask(){
    if(confirm("are you sure you want to clear?")){
        localStorage.clear()
    let list = document.getElementById("tasklist");
    list.innerHTML= "";
    let counterText = document.getElementById("counter");
    counterText.innerHTML=""
    let input = document.getElementById("taskInput");
    input.value=""
    allTask=[];
    counter=0;
    }
    
  }
  // IMPORTANT: assign the function, don't call it immediately
  window.onload = loadFromLocalStorage;

