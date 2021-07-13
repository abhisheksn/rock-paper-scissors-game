# game.py
import random

print("Rock, Paper, Scissors, Shoot!")

#Ask for a User Input
#source:
user_input = input("Please choose either 'rock', 'paper', or 'scissors': ")
print("You chose:", user_input)

#Validate the User Input
if (user_input == "rock") or (user_input == "paper") or (user_input == "scissors"):
    print("VALID")
else:
    print("OOPS!, INVALID, Please try again!")
    exit()

#Generate a Computer Choice
#source: https://www.w3schools.com/python/ref_random_choice.asp

valid_options = ["rock", "paper", "scissors"]

computer_choice = random.choice(valid_options)

print("Computer chose:", computer_choice)

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
  result_display = "Oh no! The computer won. Try again?"

print(result_display)
#Display final results
