import unittest
from two_sum import Solution


class TestLC(unittest.TestCase):

    def test_case_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        sol = Solution()
        expected_list = [0, 1]
        self.assertEqual(expected_list, sol.twoSum(nums, target))

    def test_case_2(self):
        nums = [3, 2, 4]
        target = 6
        expected_list = [1, 2]
        sol = Solution()
        self.assertEqual(expected_list, sol.twoSum(nums, target))

    def test_case_3(self):
        nums = [4, 7, 11, 4, 15]
        target = 8
        sol = Solution()
        expected_list = [0, 3]
        self.assertEqual(expected_list, sol.twoSum(nums, target))

    def test_case_4(self):
        nums, target = [1, 3, 4, 2], 6
        sol = Solution()
        expected_list = [2, 3]
        self.assertEqual(expected_list, sol.twoSum(nums, target))


if __name__ == '__main__':
    unittest.main()
