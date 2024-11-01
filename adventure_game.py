import time 
import random 

# Pause the program for 0.5 seconds and print the specified string
def print_pause(string):
    print(string)
    time.sleep(0.5)

# Display the player's score
def display_score(score):
    print_pause(f"Your score is now {score}.\n")

# Display the initial text of the game
def intro():
    print_pause("Welcome to the adventure game!")
    print_pause("In this game, you will explore a magical world filled with wonders and dangers.")
    print_pause("Your goal is to collect magical items and defeat monsters to earn points and become the greatest adventurer of all time!")
    print_pause("Are you ready to begin your adventure?\n")

# Get the user's input choice of either visiting the house or the cave
def input_choice():
    while True:
        print_pause("Enter 1 to knock on the door of the house.")
        print_pause("Enter 2 to peer into the cave.")
        print_pause("Enter 3 to check your score.\n")
        print_pause("What would you like to do?")
        in_input = input("(Please enter 1, 2, or 3.) ")
        if in_input in ["1", "2", "3"]:
            return int(in_input)
        print_pause("Please try again.\n")

# Ask the user if they want to play again
def input_retry(score):
    while True:
        choice = input("Would you like to play again? (y/n) ")
        if choice == "y":
            print_pause("Excellent! Restarting the game ...")
            play_game()
        elif choice == "n":
            print_pause(f"Thanks for playing our game! Your final score is {score}.")
            exit()
        else:
            print_pause("Please try again.\n")

# Define the monster encounter scenario
def monster(score):
    monster_type = random.choice(["fairy", "dragon", "gorgon"])
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door opens and out steps a {monster_type}.")
    print_pause(f"Eep! This is the {monster_type}'s house!")
    print_pause("The monster attacks you!")
    print_pause("You feel a bit under-prepared for this, what with only having a tiny, rusty old magic wand.\n")
    while True:
        inner_input = input("(Would you like to (1) cast a spell or (2) run away?) ")
        if inner_input in ["1", "2"]:
            inner_input = int(inner_input)
            if inner_input == 1:
                print_pause("You do your best...")
                print_pause("but your rusty old magic wand is no match for the wicked monster.")
                print_pause("You have been defeated!")
                input_retry(score)
            elif inner_input == 2:
                print_pause("You run back into the field. Luckily, you don't seem to have been followed.\n")
                return score
        print_pause("Please try again.\n")

# Define the cave scenario
def cave(score):
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Wand of Ogoroth!")
    print_pause("You discard your rusty old magic wand and take the Wand of Ogoroth with you.")
    print_pause("You walk back out to the field.\n")
    return score + 10

# Define the main game loop
def play_game():
    score = 0
    intro()
    while True:
        in_input = input_choice()
        if in_input == 1:
            score = monster(score)
            display_score(score)
        elif in_input == 2:
            score = cave(score)
            display_score(score)
        elif in_input == 3:
            display_score(score)
        else:
            print_pause("Please try again.\n")
            continue

# Start the game
play_game()
