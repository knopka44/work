import unittest
from school import *


class TestSchool(unittest.TestCase):

    def setUp(self):
        self.school = School()
        self.lera = Students("Agrest", 1, [10, 10, 9, 10, 9])
        self.nikita = Students("Popov", 2, [6, 6, 7, 6, 7])
        self.sveta = Students('Larina', 2, [5, 5, 6, 5, 5])
        self.kate = Students("Kozlova", 3, [6, 6, 7, 6, 7])
        self.school.add_student(self.lera)
        self.school.add_student(self.nikita)
        self.school.add_student(self.sveta)
        self.school.add_student(self.kate)

    def tearDown(self):
        print('This is a unittest for School')

    def test_marks_one_student(self):
        answer = self.school.marks(5, 6)
        self.assertEqual(answer, 'Larina ')

    def test_group_one_student(self):
        answer = self.school.group(1)
        self.assertEqual(answer, 'Agrest ')

    def test_automat_one_student(self):
        answer = self.school.automat(9)
        self.assertEqual(answer, 'Agrest ')

    def test_marks_some_students(self):
        answer = self.school.marks(6, 7)
        self.assertEqual(answer, 'Popov Kozlova ')

    def test_group_some_students(self):
        answer = self.school.group(2)
        self.assertEqual(answer, 'Popov Larina ')

    def test_automat_some_students(self):
        answer = self.school.automat(5)
        self.assertEqual(answer, 'Agrest Popov Larina Kozlova ')

    def test_marks_one_student_notequal(self):
        answer = self.school.marks(6, 7)
        self.assertNotEqual(answer, 'Popov ')

    def test_group_one_student_notequal(self):
        answer = self.school.group(3)
        self.assertNotEqual(answer, 'Agrest ')

    def test_automat_one_student_notequal(self):
        answer = self.school.automat(7)
        self.assertNotEqual(answer, 'Kozlova ')

    def test_marks_some_students_notequal(self):
        answer = self.school.marks(6, 7)
        self.assertNotEqual(answer, 'Agrest Larina ')

    def test_group_some_students_notequal(self):
        answer = self.school.group(2)
        self.assertNotEqual(answer, 'Agrest Kozlova ')

    def test_automat_some_students_notequal(self):
        answer = self.school.automat(6)
        self.assertNotEqual(answer, 'Agrest Larina ')


if __name__ == "__main__":
    unittest.main()
