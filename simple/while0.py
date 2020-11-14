number = 23
running = True
while running: # Поки running = True виконувати цикл
    guess = int(input('Введіть число:'))

    if guess == number:
        print ('Вітаю, ви вгадали')
        running = False # Завершення циклу
    elif guess < 0:
        print ('від\'ємні числа не підходять')
    elif guess < number:
        print ('Ні, число більше')
    else:
        print ('число менше')
else:
    print ('Цикл закінчено')
print ('Кінець')