import unittest
from rotateArray import Solution3


class TestRotateArray(unittest.TestCase):

    def test_case_1(self):
        sol = Solution3()
        test_array = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        sol.rotate(test_array, k)
        expected_list = [5, 6, 7, 1, 2, 3, 4]
        self.assertEqual(expected_list, test_array)

    def test_case_2(self):
        sol = Solution3()
        test_array = [-1, -100, 3, 99]
        k = 2
        sol.rotate(test_array, k)
        expected_list = [3, 99, -1, -100]
        self.assertEqual(expected_list, test_array)


if __name__ == '__main__':
    unittest.main()
