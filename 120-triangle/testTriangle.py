import unittest
from Triangle import Solution

class TestTriangle(unittest.TestCase):

    def test_case_1(self):
        triangle = [ [2], [3,4], [6,5,7], [4,1,8,3] ]
        sol = Solution()
        self.assertEqual(11, sol.minimumTotal2(triangle))

if __name__ == '__main__':
    unittest.main()