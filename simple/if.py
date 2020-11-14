number = 37
guess = int(input('Введіть число: '))

if guess == number:
    print ('Вітаю, ви вгадали,')
    print ('(хоча і нічого не виграли)')
elif guess < number:
    print ('число трохи більше')
else:
    print ('число трохи менше')
