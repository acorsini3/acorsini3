#set the secret number
import random
secret_number = random.randint(1,100)

#initializing attempt count
attempt = 1

#start the game
try:
    guess = input("Guess the secret number between 1 and 100 : ")
    while guess != secret_number:

      if int(guess) < int(secret_number):
        attempt = attempt+1
        print("The secret number is bigger")
        guess = input("Guess the secret number between 1 and 100 : ")
        if int(guess) == int(secret_number):
          break

      elif int(guess) > int(secret_number):
        attempt = attempt+1
        print("The secret number is smaller")
        guess = input("Guess the secret number between 1 and 100 : ")
        if int(guess) == int(secret_number):
          break
#manage exception
except:
  print("Couldn't convert your input to a valid number")
  print("Game is over")
  quit()   
#ending the game
print("You found the secret number after " + str(attempt) + " attempts" )
print("Congratulations")