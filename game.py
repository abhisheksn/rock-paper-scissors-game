# game.py
#source:https://www.w3schools.com/python/ref_random_choice.asp
import random
#source: code from https://github.com/prof-rossetti/my-first-python-app
import os
from dotenv import load_dotenv  # source:https://github.com/theskumar/python-dotenv

load_dotenv()  #invokes / uses the function we got from the third-party package. this one happens to read env vars from the ".env" file. see the "python-dotenv" package docs for more info

# uses the os module to read the specified environment variable and store it in a corresponding python variable
user_name = os.getenv("PLAYER_NAME", default="Player One")

#Ask for a User Input

user_input = input("Please choose either 'rock', 'paper', or 'scissors': ")
user_input = user_input.lower() #From Alex's question in class

#Validate the User Input
if (user_input == "rock") or (user_input == "paper") or (user_input == "scissors"):
    print("Valid input.")
else:
    print("Oops! that's an invalid input. Please try again!")
    exit()

#Generate a Computer Choice
#source: https://www.w3schools.com/python/ref_random_choice.asp

valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)

#Determine the winner

if user_input == computer_choice:
# source: https://www.programiz.com/python-programming/input-output-import
  result_display = ("Both players selected {}. The game is a tie.".format(user_input))
elif user_input == "rock" and computer_choice == "scissors":
  result_display = "Rock smashes scissors. Congrats! You won."
elif user_input == "paper" and computer_choice == "rock":
  result_display = "Paper covers rock. Congrats! You won."
elif user_input == "scissors" and computer_choice == "paper":
  result_display = "Scissors cuts paper. Congrats! You won."
else:
  result_display = "Oh, the computer won. It's ok. Try again?"

#Display final results

print("------------------")
# source: https://www.programiz.com/python-programming/input-output-import
print("Welcome {} to my Rock, Paper, Scissors game. Let's play!" .format(user_name))
print("------------------")
print("Rock, Paper, Scissors, Shoot!")
print("------------------")
print("You chose:", user_input)
print("The computer chose:", computer_choice)
print("------------------")
print(result_display)
print("------------------")
# source: https://www.programiz.com/python-programming/input-output-import
print("{}, thanks for playing. Please try again if you liked it.".format(user_name))
