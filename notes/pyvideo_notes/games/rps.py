import random
import time

print("IKentertainment Rock, Paper, Scissors")

options = ("rock", "paper", "scissors")
running = True

while running:

    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter Rock, paper, or scissors: ").lower()

    time.sleep(1)
    print("...")
    time.sleep(3)

    print(f"You: {player}")
    print(f"Computer: {computer}")

    if player == "rock" and computer == "scissors":
        print(f"YOU WON! You picked {player}")
    elif player == "scissors" and computer == "rock":
        print(f"YOU LOST! Computer picked: {computer}")
    elif player == "paper" and computer == "rock":
        print(f"YOU WON! You picked {player}")
    elif player == "rock" and computer == "paper":
        print(f"YOU LOST! Computer picked: {computer}")
    elif player == "scissors" and computer == "paper":
        print(f"YOU WON! You picked {player}")
    elif player == "paper" and computer == "scissors":
        print(f"YOU LOST! Computer picked: {computer}")
    else:
        print("ITS A TIE!")
    play_again = input("Play again? (Y/N): ").lower()
    if not play_again == "y":
        running = False

print("Thanks for playing!")