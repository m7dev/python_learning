x= 5

def func(x):
    print ('Глобальне х =', x)
    x = 2 # Локальне х
    print ('Локальне х =', x)

func(x)
print ('Глобальне залишилось =', x)

