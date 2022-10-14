def get_student_with_more_classes(Student1, Student2):
    if Student1.get_num_classes() > Student2.get_num_classes():
        return Student1.name
    elif Student1.get_num_classes() < Student2.get_num_classes():
        return Student2.name
    else:
        return f"{Student1.name} and {Student2.name} have the same number of classes."