import zipfile, time, os

#Вказуєм на папки, для резервного копіювання
source = ['C:\\TestPy\\Data']

#Вказуєм на папку в якій будуть зберігатись резервні копії
target_dir = 'C:\\TestPy\\Backup'

#Файли в архів з назвою теперішньої дати
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

#Питаєм коментар користувача
comment = input('Введіть коментар до даних резервної копії -->')
if len(comment) == 0: #якщо комент не введений
    backup = today + os.sep + now + '.zip'
else:
    backup = today + os.sep + now + '_' + comment.replace(' ','_') + '.zip'

#Створюємо папку
if not os.path.exists(today):
    os.mkdir(today) #створення папки
print('Папка успішно створена', today)


def get_all_file_paths(source): 
  
    # initializing empty file paths list 
    file_paths = [] 
  
    # crawling through source and subdirectories 
    for root, files in os.walk(source): 
        for filename in files: 
            # join the two strings in order to form the full filepath. 
            filepath = os.path.join(root, filename) 
            file_paths.append(filepath) 
    # returning all file paths 
    return file_paths

def main(): 
    # calling function to get all file paths in the source 
    file_paths = get_all_file_paths(source) 
  
    # printing the list of all files to be zipped 
    print('Following files will be zipped:') 
    for file_name in file_paths: 
        print(file_name) 
  
    # writing files to a zipfile 
    with ZipFile(backup,'w') as zip: 
        # writing each file one by one 
        for file in file_paths: 
            zip.write(file) 
  
    print('All files zipped successfully!')

if __name__ == "__main__": 
    main() 