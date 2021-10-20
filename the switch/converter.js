//intro
var choice = window.prompt("Do you want to convert something ? Y or N");
while (choice == "Y") {

    var user_input1 = window.prompt("What do you want to convert ? celsius, CHF or Liters ? :");

    //choice 1
    if (user_input1 == "celsius") {
        var user_input2 = window.prompt("Enter a temperature in celsius :");

        function conv(celsius) {
            var farenheit = (celsius * 9 / 5) + 32;
            return farenheit;
        }
        console.log("The equivalent in Farenheit is ");
        console.log(conv(user_input2));
        var choice = window.prompt("Do you want to convert something esle ? Y or N");
    }

    //choice 2
    if (user_input1 == "CHF") {
        var user_input2 = window.prompt("Enter an amount in CHF :");

        function conv(CHF) {
            var EUR = (CHF * 0.93);
            return EUR;
        }
        console.log("The equivalent in EUR is ");
        console.log(conv(user_input2));
        var choice = window.prompt("Do you want to convert something else ? Y or N");
    }

    //choice 3
    if (user_input1 == "Liters") {
        var user_input2 = window.prompt("Enter an quatity in Liters :");

        function conv(Liters) {
            var Gallons = (Liters * 0.264);
            return Gallons;
        }
        console.log("The equivalent in Gallons is ");
        console.log(conv(user_input2));
        var choice = window.prompt("Do you want to convert something else ? Y or N");
    }

    //manage exception
    if (user_input1 != "Celsius" && user_input1 != "CHF" && user_input1 != "Liters") {
        console.log("The value you entered is not valid");
    }
}
//exiting the converter
if (choice == "N") {
    console.log("Good Bye !")
}
//managing exception
if (choice != "Y" && choice != "N") {
    console.log("The value you entered is not valid")
}