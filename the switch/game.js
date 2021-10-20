let secret_number = Math.floor(Math.random() * 100);
let attempt = 1;

try {
    guess = window.prompt("Guess the secret number between 1 and 100 : ");
    if (isNaN(guess)) throw "not a number";
    while (parseInt(guess, 10) != parseInt(secret_number, 10)) {

        if (parseInt(guess, 10) < parseInt(secret_number, 10)) {
            attempt = attempt + 1;
            console.log("The secret number is bigger");
            guess = window.prompt("Guess the secret number between 1 and 100 : ");
            if (parseInt(guess, 10) == parseInt(secret_number, 10)) {
                break;
            }
        }
        if (parseInt(guess, 10) > parseInt(secret_number, 10)) {
            attempt = attempt + 1;
            console.log("The secret number is smaller");
            guess = window.prompt("Guess the secret number between 1 and 100 : ");
            if (parseInt(guess, 10) == parseInt(secret_number, 10)) {
                break;
            }
        }
    }
} catch {
    console.log("Couldn't convert your input to a valid number");
    console.log("Game is over");
    throw new Error("Something went badly wrong!");
}
console.log("You found the secret number after " + attempt + " attempts");
console.log("Congratulations");