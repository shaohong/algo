import unittest
from searchInRotatedSortedArray import Solution


class TestRotateArray(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [4,5,6,7,0,1,2]
        target = 0

        result_index = sol.search(nums, target)
        expected_index = 4
        self.assertEqual(expected_index, result_index)

    def test_case_2(self):
        sol = Solution()
        nums = [4,5,6,7,0,1,2]
        target = 3

        result_index = sol.search(nums, target)
        expected_index = -1
        self.assertEqual(expected_index, result_index)

    def test_case_empty_array(self):
        sol = Solution()
        nums = []
        target = 3

        result_index = sol.search(nums, target)
        expected_index = -1
        self.assertEqual(expected_index, result_index)

    def test_case_4(self):
        sol = Solution()
        nums = [1,3]
        target = 1

        result_index = sol.search(nums, target)
        expected_index = 0
        self.assertEqual(expected_index, result_index)

if __name__ == '__main__':
    unittest.main()
