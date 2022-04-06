import shelve

with open('pap.txt') as book:
    lines = book.readlines()
        
shelf = shelve.open('books')
shelf['Pride and Prejudice'] = lines
shelf.close()

