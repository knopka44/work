import pytest
from test_j_info import School, Students


@pytest.fixture(scope='class')
def students():
    print('\nAdding students to school')
    school = School()
    lera = Students("Agrest", 1, [10, 10, 9, 10, 9])
    nikita = Students("Popov", 2, [6, 6, 7, 6, 7])
    sveta = Students('Larina', 2, [5, 5, 6, 5, 5])
    kate = Students("Kozlova", 3, [6, 6, 7, 6, 7])
    school.add_student(lera)
    school.add_student(nikita)
    school.add_student(sveta)
    school.add_student(kate)
    yield school
    del school.students[:]
    print('\nThere is no any student at school')