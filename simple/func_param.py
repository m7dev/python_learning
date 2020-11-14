def printMax(a,b):
    if a == b:
        print ('Числа одинакові')
    elif a < b:
        print (b, 'більше', a)
    else:
        print (a, 'більше', b)

x = input ('Введіть 1-ше значення:')
y = input ('Введіть 2-ге значення:')
printMax(x,y)