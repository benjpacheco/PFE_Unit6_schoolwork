import shelve

def pctIncrease(begin, end):
    return 100*(end/begin-1)

shelf = shelve.open('cpi')
cpi = shelf['cpi']
shelf.close()


maxIncrease = 0
for year in range(1913, 2009):
    increase = pctIncrease(cpi[year][5], cpi[year][9])

    if increase > maxIncrease:
        maxIncrease = increase
        maxYear = year

print(maxYear, maxIncrease)
