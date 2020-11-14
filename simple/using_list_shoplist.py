shoplist = [] #Порожній Список
print('Список покупок', shoplist)

many = ' '
def logic(): #Створюємо функцію для логіки слова покупки 
    global many
    a = len(shoplist) 
    if a == 1:
        many = 'покупку'
    elif a == 2 or a == 3 or a == 4:
        many = 'покупки'
    elif a >= 5 and a <= 20:
        many = 'покупок'
    else:
        many = 'покупок(ки)'

logic()
print ('Я маю купити', len(shoplist), many)

running = True
while running:
    print('\n(Для виходу введіть "нічого", або натисніть "Enter")')
    plus = input ('Що ще потрібно купити?: ')
    if plus == ' ' or plus == 'нічого' or plus == '' or plus == "Enter":
        print('Добре, дякую!')
        running = False
    else:
        shoplist.append(plus)
print('\nТепер мій список покупок виглядає так:', shoplist)

logic()
print('Я маю купити', len(shoplist), many)

shoplist.sort()
print('\nВідсортований список покупок:', shoplist)