import nltk
import enchant
import random

print("IKwords")
nltk.download('words', quiet=True)
from nltk.corpus import words

# Initialize the dictionary and get the list of valid 5-letter words
dictionary = enchant.Dict("en_US")
word_list = [word.lower() for word in words.words() if len(word) == 5 and dictionary.check(word)]

# Choose a random word as the answer
word = random.choice(word_list)

# Game state
running = True
guesses = 0
max_guesses = 6

print("\nGuess the 5-letter word! You have 6 tries.\n")
print("If the letter has () around it, it is in the word. \nIf it has [] around it, it is in the correct spot. \nIf it has nothing around it, it is not in the word.")

while running and guesses < max_guesses:
    guess = input(f"Attempt {guesses + 1}: ").lower()
    
    if len(guess) != 5:
        print("Please enter exactly 5 letters.")
        continue
    
    if not dictionary.check(guess):
        print("Not a valid word. Try again.")
        continue
    
    # Display feedback
    feedback = []
    for i, char in enumerate(guess):
        if char == word[i]:
            feedback.append(f"[{char.upper()}]")  # Correct spot
        elif char in word:
            feedback.append(f"({char})")          # Wrong spot
        else:
            feedback.append(char)                 # Not in word
    
    print("Feedback: " + " ".join(feedback))
    
    guesses += 1
    
    if guess == word:
        print("\n🎉 Congratulations! You guessed the word!")
        running = False
    elif guesses == max_guesses:
        print(f"\n❌ Out of guesses! The word was: {word}")

print("\nThanks for playing IKwords!")
