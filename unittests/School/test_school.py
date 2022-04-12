import unittest
from school import *


class TestSchool(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.school = School()
        lera = Students("Agrest", 1, [10, 10, 9, 10, 9])
        nikita = Students("Popov", 2, [6, 6, 7, 6, 7])
        sveta = Students('Larina', 2, [5, 5, 6, 5, 5])
        kate = Students("Kozlova", 3, [6, 6, 7, 6, 7])
        cls.school.add_student(lera)
        cls.school.add_student(nikita)
        cls.school.add_student(sveta)
        cls.school.add_student(kate)

    @classmethod
    def tearDownCLass(cls):
        print('This is a unittest for School')

    def test_add_student(self):
        answer = len(self.school.students)
        self.assertEqual(answer, 4)

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

    def test_add_student_notequal(self):
        answer = len(self.school.students)
        self.assertNotEqual(answer, 2)

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

    def test_marks_args(self):
        with self.assertRaises(AssertionError) as er:
            self.school.marks(6)
        self.assertEqual('please enter more than 1 mark', er.exception.args[0])

    def test_group_int(self):
        with self.assertRaises(AssertionError) as er:
            self.school.group('1')
        self.assertEqual('group must be int', er.exception.args[0])

    def test_automat_int(self):
        with self.assertRaises(AssertionError) as er:
            self.school.automat('5')
        self.assertEqual('automat must be int', er.exception.args[0])


if __name__ == "__main__":
    unittest.main()
