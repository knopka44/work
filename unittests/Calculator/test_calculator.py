import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calc = Calculator()

    @classmethod
    def tearDownClass(cls):
        print('This is a unittest for calculator')

    def test_sum(self):
        answer = self.calc.sum(15, 4)
        self.assertEqual(answer, 19)

    def test_sub(self):
        answer = self.calc.sub(26, 6)
        self.assertEqual(answer, 20)

    def test_mult(self):
        answer = self.calc.mult(7, 3)
        self.assertEqual(answer, 21)

    def test_div(self):
        answer = self.calc.div(22, 11)
        self.assertEqual(answer, 2)

    def test_sum_not_eq(self):
        answer = self.calc.sum(6, 10)
        self.assertNotEqual(answer, 15)

    def test_sub_not_eq(self):
        answer = self.calc.sub(33, 3)
        self.assertNotEqual(answer, 36)

    def test_mult_not_eq(self):
        answer = self.calc.mult(8, 8)
        self.assertNotEqual(answer, 60)

    def test_div_not_eq(self):
        answer = self.calc.div(55, 11)
        self.assertNotEqual(answer, 7)

    def test_div_y_zero(self):
        with self.assertRaises(AssertionError) as er:
            self.calc.div(7, 0)
        self.assertEqual('y must not be 0', er.exception.args[0])

    def test_validation(self):
        with self.assertRaises(AssertionError) as er:
            self.calc.validation(15, '6')
        self.assertEqual('x or y must be int', er.exception.args[0])


if __name__ == "__main__":
    unittest.main()
