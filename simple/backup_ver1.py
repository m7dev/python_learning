import os
import time

#Вказуєм на папки, для резервного копіювання
source = ['C:\\TestPy\\Data', '"C:\\TestPy\\my wallpaper"']

#Вказуєм на папку в якій будуть зберігатись резервні копії
target_dir = 'C:\\TestPy\\Backup'

#Файли в архів з назвою теперішньої дати
backup = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

#Команда zip
zip_command = "zip -qr {0} {1}".format(backup, ' '.join(source))

print(zip_command)
#Створення резервної копії
if os.system(zip_command) == 0:
    print ('Резервна копія створена в', backup)
else:
    print('Резервну копію НЕ СТВОРЕНО!!')