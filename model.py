from pathlib import Path
import os
# main_path = Path.cwd()
uni_path = Path('Seminar08', 'lists')
classes_names = {}
class_data = {}


def reab_db(current_class_name: str):
    global class_data
    current_file_name = current_class_name+'.txt'
    path = Path(uni_path, current_file_name)
    # print(f'Прочитать данные класса {path}')
    with open(path, 'r', encoding='UTF-8') as file:
        file_data = file.read()
        class_summary_data = list(filter(lambda x: (x!=''),file_data.replace('\n','').split('#')))
        
        for subject in class_summary_data:
            subject_summary_data = subject.split(':')
            subject_name = subject_summary_data[0]
            subject_data = list(filter(lambda x: (x!=''),subject_summary_data[1].split(')')))

            class_data[subject_name] = {}

            for student in subject_data:
                student_summary_data = student.split('(')

                student_name = student_summary_data[0]
                student_grades = student_summary_data[1].split(',')
                class_data[subject_name][student_name] = student_grades

def get_students_grades(local_subject, local_student):
    local_grades = class_data[local_subject][local_student]
    return local_grades



def write_db(current_path: str):
    pass


def get_classes_names(current_path: str):
    files_list = os.listdir(current_path)
    global classes_names
    for file_number, file_name in enumerate(files_list):
        classes_names[file_number+1] = file_name.split('.')[0]
