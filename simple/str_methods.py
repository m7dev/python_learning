name = 'Михайло' #Вгадуванння імені

if name.startswith('Ми'):
    print('Так, ім\'я має склад "Ми"')
if 'а' in name:
    print('Так, ім\'я має букву "а"')
if name.find('о'):
    print('Так, ім\'я має букву "o"')

delim = '! ' #delimiter - роздільник

mylist = ['Ukraine', 'Germany', 'Italy', 'France', ' ']
print(delim.join(mylist))

