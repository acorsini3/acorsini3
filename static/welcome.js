// works with golf.html

const addButton = document.getElementById("addButton");
addButton.className = "addButton";

const content = document.getElementById("content");
content.className = "appStyle";

const myText = document.getElementById("myText");

// not in the function because I need to store only one name
const newName = document.createElement("p");
newName.className = "newElement";
newName.innerText = localStorage.getItem("username");

//The welcome message
const welcome = document.createElement("p");
if (performance.navigation.type == performance.navigation.TYPE_RELOAD) {
    welcome.innerText = "Welcome back "
} else { welcome.innerText = "Welcome " }
content.appendChild(welcome);


// add the username in the local storage then display it on the screen
function addName() {
    const data = myText.value;
    data.classeName = "newElement";
    localStorage.setItem('username', data);

    //location.reload();
}
content.appendChild(newName);
addButton.addEventListener("click", addName);