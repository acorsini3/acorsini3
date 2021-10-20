# first choice
choice1 = input("Do you want to convert something ? Y or N ")
# manage exception
if choice1 !="Y" and choice1 !="N":
    print("The value you entered is not valid")
    quit()
#second choice
while choice1 == "Y":
    choice2 = input("What do you want to convert ? celsius, CHF or liters ? ")
    #conversion
    if choice2 == "celsius" :
        celsius= int(input("Enter a tmperature in celsius : "))
        farenheit = float((celsius *9/5)+32)
        print("The equivalent in farenheit is "+ str(farenheit))
        choice1 = input("Do you want to convert something ? Y or N ")
    elif choice2 == "CHF" :
        CHF= int(input("Enter an amount in CHF : "))
        EUR = float(CHF *0.93)
        print("The equivalent in EURO is "+ str(EUR))
        choice1 = input("Do you want to convert something ? Y or N ")
    elif choice2 == "liters" :
        liters= int(input("Enter a quantity in liters : "))
        galons = float(liters *0.264)
        print("The equivalent in galons is "+ str(galons))     
        choice1 = input("Do you want to convert something ? Y or N ")   
    #manage exception
    elif choice2 != "celius" and choice2!= "CHF" and choice2!= "liters":
        print("The value you entered is not valid")
        quit()

if choice1 == "N":
    print("Good Bye ! ")


