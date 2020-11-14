def printMax(a,b):
    if a == b:
        print ('Числа одинакові')
    elif a < b:
        print (b, 'більше', a)
    else:
        print (a, 'більше', b)
x = int(input ('Введіть 1-ше значення:'))
y = 10
printMax(x,y)