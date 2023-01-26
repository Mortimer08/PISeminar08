import view
import model

def start():
    print('Start')
    model.get_classes_names('/home/mort/GB Study Projects/PythonIntroducing/Seminar08/lists')
    view.classes_list(model.classes_names)
    choosed_class_number = view.class_id()
    if choosed_class_number in model.classes_names.keys():
        model.reab_db(model.classes_names[choosed_class_number])
