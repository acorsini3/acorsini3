const content = document.getElementById("content");

var init = 1;

console.log(init);
localStorage.setItem(init, "A");
init = init + 1;
console.log(init);

localStorage.setItem(init, "B");
init = init + 1;
console.log(init);

localStorage.setItem(init, "C");

init = init - 1;
console.log(init);

const test = (localStorage.getItem(init));
console.log(test);

const newParagraph = document.createElement("p");
newParagraph = toString(localStorage.getItem(init));
document.innerHTML(newParagraph);
//content.appendChild(newParagraph);