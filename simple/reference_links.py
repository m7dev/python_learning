print('Просте присвоювання') # Виведе одинакові значення об'єкта
shoplist = ['яблука', 'молоко', 'морква', 'банани']
mylist = shoplist #milist - ще одно ім'я, яке вказує на той самий об'єкт

del shoplist[0] #Видаляєм перший елемент списку

print('shoplist:', shoplist) 
print('mylist:', mylist)

###

print('Копіювання повною вирізкою') #Виведе різний результат
mylist = shoplist[:] 
del mylist[0]

print('shoplist:', shoplist)
print('mylist:', mylist)