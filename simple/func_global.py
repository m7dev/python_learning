x= 5

def func():
    global x
    print ('Глобальне х =', x)
    x = 2 # Локальне х
    print ('Локальне х =', x)

func()
print ('Глобальне x змінилось =', x)

