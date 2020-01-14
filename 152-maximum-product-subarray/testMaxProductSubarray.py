import unittest
from MaxProductSubarray import Solution

class TestLC(unittest.TestCase):

    def test_case_1(self):
        test_list = [2,3,-2,4]
        sol = Solution()
        self.assertEqual(6, sol.maxProduct(test_list))

    def test_case_2(self):
        test_list = [-2,0,-1]
        sol = Solution()
        self.assertEqual(0, sol.maxProduct(test_list))

if __name__ == '__main__':
    unittest.main()