import unittest
from LongestIncreasingSubsequence import Solution


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        test_sequence = [10, 9, 2, 5, 3, 7, 101, 18]
        sol = Solution()
        self.assertEqual(4, sol.lengthOfLIS(test_sequence))


if __name__ == '__main__':
    unittest.main()
