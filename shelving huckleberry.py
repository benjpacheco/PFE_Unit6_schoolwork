import urllib.request, shelve

url = ' http://nancymcohen.com/csci133/hf.txt'
book = urllib.request.urlopen(url)
lines = book.readlines()
book.close()

finalLines = [line.decode()[:-2] for line in lines[21:11381]]

shelf = shelve.open('books')
shelf['Huckleberry Finn'] = finalLines
shelf.close()
