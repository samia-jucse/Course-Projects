function loadTask() {
    let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    tasks.forEach((task) => addTaskToDOM(task));
}
function addTask() {
    let textInput = document.getElementById("taskInput");
    let taskValue = textInput.value.trim();
    if (taskValue === "") {
        alert("Please enter a task!");
        return;
    }
    let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    addTaskToDOM(taskValue);
    tasks.push(taskValue);
    localStorage.setItem("tasks", JSON.stringify(tasks));

    textInput.value = "";
}

function addTaskToDOM(taskValue) {
    let ul = document.getElementById("taskList");

    let li = document.createElement("li");
    li.innerHTML = `<span>${taskValue}</span>
    <span>
            <span class="delete btn btn-danger" onclick="deleteTask(this)" >Delete</span>
        </span>`

    ul.appendChild(li);
}
function deleteTask(element) {
    let li = element.parentElement.parentElement;
    let taskText = li.firstElementChild.innerText;

    li.remove()

    let tasks = JSON.parse(localStorage.getItem("tasks")) || []
    tasks = tasks.filter(task => task !== taskText)
    localStorage.setItem("tasks",JSON.stringify(tasks))
}
document.addEventListener('DOMContentLoaded', loadTask);

