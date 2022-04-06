def f(x):
    return 17.7/(4*x**2-12*x+13)

def xValues(begin, end, number):
    step = (end-begin)/(number-1)
    return [begin+n*step for n in range(number)]

begin = float(input('Enter beginning number: ' ))
end = float(input('Enter end number: ' ))
print(max([f(x) for x in xValues(begin, end, 100)]))
