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


#Display final results
