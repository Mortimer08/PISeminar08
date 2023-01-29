def classes_list(local_classes_dict):
    print('Классы в базе')
    for class_number, class_name in local_classes_dict.items():
        print(f'\t{class_number}. {class_name}')


def choosen_class_number() -> int:
    while True:
        class_number = input('\nВыберите номер класса для работы: ')
        if class_number.isdigit():
            return int(class_number)

# def show_subjects(class_data: dict):
#     print()
#     print('Предметы:\n')
#     for number, subject in enumerate(class_data.keys()):
#         number +=1
#         print(f'{number}. {subject}')
        # for student in class_data[subject].keys():
        #     grades_list = class_data[subject][student]
        #     print(f'{student}: {grades_list}')

# def show_students(class_data: dict, local_subject_name):
#     for student in class_data.keys():
#         print(f'\tПредемет: {subject}')
#         for student in class_data[subject].keys():
#             grades_list = class_data[subject][student]
#             print(f'{student}: {grades_list}')
#         print()


def choosen_subject(class_data: dict) -> str:
    print()
    print('Предметы:\n')
    subjects = []
    for number, subject in enumerate(class_data.keys(), 1):
        print(f'\t{number}. {subject}')
        subjects.append([number, subject])
    while True:
        subject_number = input('\nВыберите номер предмета для работы: ')
        if subject_number.isdigit():
            return subjects[int(subject_number)-1][1]


def choosen_student(subject_data: dict) -> str:
    print()
    print('Ученики:\n')
    students = []
    for number, student in enumerate(subject_data.keys(), 1):
        print(f'\t{number}. {student}')
        students.append([number, student])
    while True:
        student_number = input('\nВыберите номер ученика для работы: ')
        if student_number.isdigit():
            return students[int(student_number)-1][1]


def show_choosen_student(local_student_name, grades):
    print(f'{local_student_name}: {", ".join(grades)}')


def show_subject_info():

    pass
