print("IKessentials Dice roller")

import random


running = True

while running:

    dice_art = {
        1: ("┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘"),
        2: ("┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘"),

        3: ("┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘"),
        4: ("┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘"),
        5: ("┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘"),
        6: ("┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘")

    }

    dice = []
    total = 0
    num_of_dice = int(input("How many dice do you want to roll?: "))

    for die in range (num_of_dice):
        dice.append(random.randint(1, 6))

    for die in range(num_of_dice):
        for line in dice_art.get(dice[die]):
            print(line)

    for die in dice:
        total += die
    print(f"total: {total}")

    roll_again = input("Roll again? (y/n): ").lower()
    if not roll_again == "y":
        running == False


print("Thanks for using!")