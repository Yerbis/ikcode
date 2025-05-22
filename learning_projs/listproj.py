# For more data on lists go to notes/pybook_notes/data_structures/list.notes.py


vowels = ['a', 'e', 'i', 'o', 'u']

word = input("Provide a word to search for vowels: ")

found = []

for letter in word:
    if letter in vowels:
            if letter not in found:
                  found.append(letter)
for vowels in found:
      print(vowels)

print('=============================================')