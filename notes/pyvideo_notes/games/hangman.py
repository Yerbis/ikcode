print("IKentertainment Hangman")
import random

tried = True

while tried:
    word = input('Player 1, enter a word for player 2 to guess: ').lower()

    if not word.isalpha():
        print("Word cannot contain digits")
        tried = True
    else:
        tried = False


print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")

art = {0:("   ",
          "   ",
          "   "),
       1:(" o ",
          "   ",
          "   "), 
       2:(" o ",
          " | ",
          "   "), 
       3:(" o ",
          "/| ",
          "   "
          ), 
       4:(" o ",
          "/|\\",
          "   "),
       5:(" o ",
          "/|\\",
          "/  "), 
       6:(" o ",
          "/|\\",
          "/ \\")}

def display_man(wrong_guesses):
    print("========================================")
    for line in art[wrong_guesses]:
        print(line)
    print("========================================")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = word
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Player 2, guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid guess.")
            continue

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        
        elif guess not in answer:
            wrong_guesses += 1
        
        if wrong_guesses > 7:
            is_running = False

    if wrong_guesses > 7:
        print("You lost!")

if __name__ == "__main__":
    main()


