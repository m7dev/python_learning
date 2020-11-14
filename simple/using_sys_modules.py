#$ python3 using_sys_modules.py we are arguments 
# << аргументи модуля
import sys
print ('Просто текст')
for i in sys.argv:
    print(i)

print('\n\nЗмінна PYTHONPATH має', sys.path, '\n')