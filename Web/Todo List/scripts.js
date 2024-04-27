const taskSource = document.getElementById("task-source");
const taskList = document.getElementById("task-list");

function addTask() {
    const newTask = document.createElement("div");
    newTask.classList.add("task");

    const textBox = document.createElement("p");
    const taskText = document.createTextNode(taskSource.value);
    textBox.classList.add("task-text");
    textBox.appendChild(taskText);
    newTask.appendChild(textBox); 

    const newButton = document.createElement("button");
    const buttonText = document.createTextNode("✖");
    newButton.setAttribute("onclick", "deleteTask(this)");
    newButton.classList.add("task-delete");
    newButton.appendChild(buttonText);
    newTask.appendChild(newButton);

    taskList.appendChild(newTask);
    taskSource.value = "";

    console.log(newTask);
}

function deleteTask(caller) {
    caller.parentElement.remove();
}