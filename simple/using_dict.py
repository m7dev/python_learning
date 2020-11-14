ab = {  'Mykhailo': '0987283007', #Словник
        'Bogdana' : '0982347191',
        'Tetyana' : '0973245123',
        'Spammer' : '1234988543'
     }
print(ab['Mykhailo']) #Друкує елемент словника

del ab['Spammer'] #Видаляє елемент словника

def allbook(): #Створюємо функцію для виведення всієї адресної книги
    for name, address in ab.items():
        print('Контакт {0} з номером {1}'.format(name, address))


ab['Somebody'] = '0972345243' #Добавляєм елемент в словник
print('\nВ адресній книзі {0} контакти\n'.format(len(ab)))

allbook()

findname = input('\nВведіть ім\'я яке шукаєте: ') #Пошук по словнику
print('Телефон {0}: {1}'.format(findname, ab[findname]))