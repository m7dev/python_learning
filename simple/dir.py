import sys 
print(dir(sys)) #Список атрибутів модуля sys
print('\n')
print(dir()) #Список атрибутів для теперішнього модуля (список імпортованих модулів теж входить (sys))
a = 5 #Нова змінна
print('\n Добавим змінну')
print(dir())