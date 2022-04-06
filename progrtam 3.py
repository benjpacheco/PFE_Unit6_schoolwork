import my, shelve

def averageWordLength(title):
    
    shelf = shelve.open('books')
    lines = shelf[title] 
    shelf.close()

    number = 0
    totalLength = 0

    for line in lines:
        for word in my.cleanedup(line).split():
            number += 1
            totalLength += len(word)
    return totalLength/number

for title in ['Pride and Prejudice', 'Huckleberry Finn']:
    print(title, averageWordLength(title))
