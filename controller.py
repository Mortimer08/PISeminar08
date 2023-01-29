import view
import model


def start():
    model.get_classes_names(
        '/home/mort/GB Study Projects/PythonIntroducing/Seminar08/lists')
    view.classes_list(model.classes_names)

    choosen_class_number = view.choosen_class_number()
    if choosen_class_number in model.classes_names.keys():
        model.reab_db(model.classes_names[choosen_class_number])
    choosen_subject = view.choosen_subject(model.class_data)
    choosen_student = view.choosen_student(model.class_data[choosen_subject])

    view.show_choosen_student(choosen_student, model.get_students_grades(
        choosen_subject, choosen_student))
    # 
