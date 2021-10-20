// works with golf4.html

const addButton = document.getElementById("addButton");
addButton.className = "button";

const content = document.getElementById("content");
content.className = "boxStyle";

const myText = document.getElementById("username"); //enter by the user in the text box

//the const welcome
const welcome = document.createElement("p");
welcome.innerText = "Welcome  "
content.appendChild(welcome);

const inputa = document.getElementById("aname"); //hidden in add score

const inputc = document.getElementById("cname"); //hidden in calculate

const newName = document.createElement("p"); //create a new paragraph
newName.className = "name"; // styling
newName.innerText = localStorage.getItem("username"); //get what is in the local storage with key username
inputa.value = localStorage.getItem("username"); //get the username in the local storage and put it in html aname
inputc.value = localStorage.getItem("username"); //get the username in the local storage and put it in html cname

// add the username in the local storage then display it on the screen
function addName() {
    const name = myText.value;
    name.className = "newElement";
    localStorage.setItem('username', name); // set the value enter by the user in the local storage with key username
    location.reload();
}

content.appendChild(newName);
addButton.addEventListener("click", addName);