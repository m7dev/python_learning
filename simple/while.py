number = 23
running = True
while running: # Поки running = True виконувати цикл
    guess = int(input('Введіть число:'))

    if guess == number:
        print ('Вітаю, ви вгадали')
        running = False # Завершення циклу
    elif guess < number:
        print ('Ні, число більше')
    else:
        print ('Ні, число менше')
else:
    print ('Цикл закінчено')
print ('Кінець')