import unittest
import numpy as np

from solution import student_ln

EPSILON = 1e-6

class PublicTests(unittest.TestCase):
    def setUp(self):
        pass

    def test1(self):
        x_hat = np.array([0.999])
        
        print("diff: ", np.log(x_hat) - np.array([student_ln(x) for x in x_hat]))
        assert np.all(
            np.abs(np.log(x_hat) - np.array([student_ln(x) for x in x_hat])) < EPSILON
        )

    def test2(self):
        assert np.abs(student_ln(np.e) - 1.0) < EPSILON

    def test3(self):
        assert float('-inf') == student_ln(0)

    def test4(self):
        self.assertRaises(ValueError, student_ln, -1)


if __name__ == "__main__":
    unittest.main()
