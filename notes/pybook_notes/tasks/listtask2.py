# For more data on lists go to notes/pybook_notes/data_structures/list.notes.py

book = "The dingus's quest"
booklist = list(book)
print(booklist)



booklist[0:3]

''.join(booklist[0:3])
''.join(booklist[-6:])

backwards = booklist[::-1]
''.join(backwards)

every_other = booklist[::2]
''.join(every_other)

''.join(booklist[4:11])
''.join(booklist[13:3:-1])