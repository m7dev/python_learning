import os
import time

#Вказуєм на папки, для резервного копіювання
source = ['C:\\TestPy\\Data', '"C:\\TestPy\\my wallpaper"']

#Вказуєм на папку в якій будуть зберігатись резервні копії
target_dir = 'C:\\TestPy\\Backup'

#Файли в архів з назвою теперішньої дати
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

#Створюємо папку
if not os.path.exists(today):
    os.mkdir(today) #створення папки
print('Папка успішно створена', today)

#Ім'я файла
backup = today + os.sep + now + '.zip'

#Команда zip
zip_command = "zip -qr {0} {1}".format(backup, ' '.join(source))

#Створення резервної копії
if os.system(zip_command) == 0:
    print ('Резервна копія створена в', backup)
else:
    print('Резервну копію НЕ СТВОРЕНО!!')