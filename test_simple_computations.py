import unittest
import numpy as np


class TestSimpleComputations(unittest.TestCase):
    def test_multiplication_of_floats(self):
        self.assertEqual(10.0 * 0.1, 1.0)

    def test_multiplication_of_floats2(self):
        self.assertEqual(0.1 * 0.1, 0.01)

    def test_multiplication_of_floats3(self):
        self.assertEqual(0.5 * 0.5, 0.25)

    def test_addition_of_two_floats(self):
        self.assertEqual(0.1 + 0.1, 0.2)

    def test_addition_of_three_floats(self):
        self.assertEqual(0.1 + 0.1 + 0.1, 0.3)

    def test_addition_of_four_floats(self):
        self.assertEqual(0.1 + 0.1 + 0.1 + 0.1, 0.4)

    def test_addition_is_associative(self):
        self.assertEqual((0.1 + 0.1) + 1, 0.1 + (0.1 + 1))

    def test_increase_through_addition(self):
        self.assertGreater(1_00000_00000_00000_00000 + 1, 1_00000_00000_00000_00000)

    def test_increase_through_addition2(self):
        self.assertGreater(1e20 + 1, 1e20)

    def test_increase_through_addition3(self):
        self.assertGreater(1e20 + 1000, 1e20)

    def test_greater_zero(self):
        self.assertGreater(0.1**25, 0)

    def test_greater_zero2(self):
        self.assertGreater(0.1**5**5, 0)

    def test_numpy_ints(self):
        large_number = 2**63 - 1
        a = np.array([large_number, large_number])
        self.assertTrue(np.all(a > 0))

    def test_numpy_ints_sum(self):
        large_number = 2**63 - 1
        a = np.array([large_number, large_number])
        self.assertGreater(np.sum(a), 0)


if __name__ == "__main__":
    unittest.main()
