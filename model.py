from pathlib import Path
import os
main_path = Path.cwd()
uni_path = Path('Seminar08','lists')
classes_names = {}
class_data = {}


def reab_db(current_class_name: str):
    global class_data
    current_file_name = current_class_name+'.txt'
    path = Path(uni_path, current_file_name)
    print(f'Прочитать данные класса {path}')
    with open(path,'r', encoding='UTF-8') as file:
        file_data = file.read()
        print(file_data)


def write_db(current_path: str):
    pass


def get_classes_names(current_path: str):
    files_list = os.listdir(current_path)
    global classes_names
    for file_number, file_name in enumerate(files_list):
        classes_names[file_number+1] = file_name.split('.')[0]
