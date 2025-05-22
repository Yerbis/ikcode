# For more data on lists go to notes/pybook_notes/data_structures/list.notes.py



vowels = ['a', 'e', 'i', 'o', 'u']

word = 'BiggestBird'

for letter in word:
    if letter in vowels:
        print(letter)