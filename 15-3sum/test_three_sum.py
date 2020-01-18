import unittest
from three_sum import Solution, Solution2


class TestLC(unittest.TestCase):
    def test_case_1(self):
        nums = [-1, 0, 1, 2, -1, -4]
        expected_list = [[-1, 0, 1], [-1, -1, 2]]
        sol = Solution()
        result = sol.threeSum(nums)
        for x in expected_list:
            self.assertIn(x, result)

class TestLC2(unittest.TestCase):
    def test_case_1(self):
        nums = [-1, 0, 1, 2, -1, -4]
        expected_list = [[-1,-1,2],[-1,0,1]]
        sol = Solution2()
        result = sol.threeSum(nums)
        print(result)
        for x in expected_list:
            self.assertIn(x, result)
        for x in result:
            self.assertIn(x, expected_list)


if __name__ == '__main__':
    unittest.main()
