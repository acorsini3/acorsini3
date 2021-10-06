// works with golf.html

const addButton = document.getElementById("addButton");
addButton.className = "button";

const content = document.getElementById("content");
content.className = "boxStyle";

const myText = document.getElementById("myText");

// not in the function because I need to store only one name
const newName = document.createElement("p"); //create a new paragraph
newName.className = "name";
newName.innerText = localStorage.getItem("username"); //get what is in the local storage with key username

//the const welcome
const welcome = document.createElement("p");
if (performance.navigation.type == performance.navigation.TYPE_RELOAD) {
    welcome.innerText = "Welcome back "
} else { welcome.innerText = "Welcome " }
content.appendChild(welcome);


// add the username in the local storage then display it on the screen
function addName() {
    const name = myText.value;
    name.classeName = "newElement";
    localStorage.setItem('username', name); // set the value enter by the user in the local storage with key username

}
content.appendChild(newName);
addButton.addEventListener("click", addName);