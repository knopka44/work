import json

with open('students.json', 'r') as file:
    py_obj = json.load(file)


def assertion(user_input):
    assert isinstance(user_input, str), f'{user_input} must be string'
    return True


def one_class_students(class_number):
    assertion(class_number)
    students = ''
    if any([class_number in element['Class'] for element in py_obj]):
        for element in py_obj:
            if element['Class'] == class_number:
                students += element['Name'] + ' / '
        print(f'{students}are in class {class_number}')
    else:
        print(f'Class {class_number} is not found')


def one_club_students(club):
    assertion(club)
    students = ''
    if any([club in element['Club'] for element in py_obj]):
        for element in py_obj:
            if element['Club'] == club:
                students += element['Name'] + ' / '
        print(f'{students}go to {club}')
    else:
        print(f'Club {club} is not found')


def one_gender(gender):
    upper_gender = gender.upper()
    genders = 'MW'
    assert upper_gender in genders, 'Gender must be M or W (type string)'
    students = ''
    for element in py_obj:
        if element['Gender'] == upper_gender:
            students += element['Name'] + ' / '
    print(f'{students}are {gender} gender')


def find_a_student_by_name(name):
    assertion(name)
    if any([name in element['Name'] for element in py_obj]):
        for element in py_obj:
            if name in element['Name']:
                print(element)
    else:
        print(f'Name {name} is not found')
