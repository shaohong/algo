import unittest
from majority_element import Solution, Solution2


class TestLC(unittest.TestCase):
    def test_case_1(self):
        nums = [3, 2, 3]
        sol = Solution()
        self.assertEqual(3, sol.majorityElement(nums))

    def test_case_2(self):
        nums = [2, 2, 1, 1, 1, 2, 2]
        sol = Solution()
        self.assertEqual(2, sol.majorityElement(nums))


class TestLC2(unittest.TestCase):
    def test_case_1(self):
        nums = [3, 2, 3]
        sol = Solution2()
        self.assertEqual(3, sol.majorityElement(nums))

    def test_case_2(self):
        nums = [2, 2, 1, 1, 1, 2, 2]
        sol = Solution2()
        self.assertEqual(2, sol.majorityElement(nums))

    def test_case_3(self):
        nums = [1]
        sol = Solution2()
        self.assertEqual(1, sol.majorityElement(nums))


    def test_case_4(self):
        nums = [3,3,4]
        sol = Solution2()
        self.assertEqual(3, sol.majorityElement(nums))
if __name__ == "__main__":
    unittest.main()
