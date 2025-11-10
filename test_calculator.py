# https://github.com/elijahbaez/lab10-EB-CW.git
# Partner 1: Elijah Baez
# Partner 2: Curtis Whipple

import unittest
import calculator

class TestCalculator(unittest.TestCase):

    # Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 4), 3)
        self.assertEqual(calculator.add(0, 0), 0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(calculator.sub(10, 4), 6)
        self.assertEqual(calculator.sub(5, 10), -5)
        self.assertEqual(calculator.sub(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(calculator.mul(3, 4), 12)
        self.assertEqual(calculator.mul(-2, 5), -10)
        self.assertEqual(calculator.mul(0, 100), 0)

    def test_divide(self):
        self.assertEqual(calculator.div(2, 10), 5)
        self.assertEqual(calculator.div(5, 10), 2)
        self.assertAlmostEqual(calculator.div(4, 1), 0.25)

    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 5)

    def test_logarithm(self):  # 3 assertions
        self.assertEqual(calculator.log(2, 8), 3)
        self.assertEqual(calculator.log(10, 100), 2)
        self.assertAlmostEqual(calculator.log(3, 27), 3)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            calculator.log(1, 5)  # base cannot be 1

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.log(-10, 100)  # Negative base
        with self.assertRaises(ValueError):
            calculator.log(10, -100)  # Negative number
        with self.assertRaises(ValueError):
            calculator.log(1, 100)  # Base of 1

    def test_hypotenuse(self):
        self.assertEqual(calculator.hypotenuse(3, 4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13)
        self.assertEqual(calculator.hypotenuse(-3, 4), 5)  # Works with negative nums

    def test_sqrt(self):
        self.assertEqual(calculator.square_root(16), 4)
        self.assertAlmostEqual(calculator.square_root(2), 1.41421356)
        with self.assertRaises(ValueError):
            calculator.square_root(-9)


# Do not touch this
if __name__ == "__main__":
    unittest.main()