import urllib.request, shelve

userInput = input('Enter query: ')
splitedInput = userInput.split(' ')

cpiYear = int(splitedInput[0])
months = splitedInput[1:13]

url = 'http://nancymcohen.com/csci133/cpiai.txt'
file = urllib.request.urlopen(url)
lines = file.readlines()
file.close()

cpi = {}
for line in lines:
    items = line.decode().split()
    if len(items) > 0 and items[0].isdigit():
        cpi[int(items[0])] = [float(item) for item in items[1:13]]

shelf = shelve.open('cpi')
shelf['cpi'] = cpi
shelf.close()

monthofYear = cpi[cpiYear]

newMonthOfTheYear = [monthofYear[int(month) - 1] for month in months]

correctMonthsOfTheYear = []
if len(months):
    correctMonthsOfTheYear = newMonthOfTheYear
else:
    correctMonthsOfTheYear = monthofYear

def averageCpi(year):
    number = 0
    total = 0

    for value in correctMonthsOfTheYear:
        total += value
        number += 1
    return total/number

maxY = max(correctMonthsOfTheYear)



print(correctMonthsOfTheYear)
print('max:', maxY)
print('avg:', averageCpi(correctMonthsOfTheYear))

