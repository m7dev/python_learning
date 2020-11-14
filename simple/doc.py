def printMax(x, y):
    ''' Виводить максимальне значення з двох цілих чисел'''
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'більше')
    else:
        print(y, 'більше')

printMax(100,3000)
print(printMax.__doc__)

help(printMax)



