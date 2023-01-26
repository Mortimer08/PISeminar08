def classes_list(local_classes_dict):
    print('Классы в базе')
    for class_number, class_name in local_classes_dict.items():
        print(f'\t{class_number}. {class_name}')

def class_id() -> int:
    while True:
        class_number = input('\nВыберите номер класса для работы: ')
        if class_number.isdigit():
            return int(class_number)