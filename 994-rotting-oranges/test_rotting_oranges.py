import unittest

from rotting_oranges import Solution


class TestLC(unittest.TestCase):

    def test_case_1(self):
        grid = [[2,1,1],[1,1,0],[0,1,1]]
        sol = Solution()
        self.assertEqual(4, sol.orangesRotting(grid))


    def test_case_2(self):
        '''
        Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
        '''
        grid = [[2,1,1],[0,1,1],[1,0,1]]
        sol = Solution()
        self.assertEqual(-1, sol.orangesRotting(grid))

    def test_case_3(self):
        '''
        Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
        '''
        grid = [[0,2]]
        sol = Solution()
        self.assertEqual(0, sol.orangesRotting(grid))

    def test_case_4(self):
        grid=[[1],[1],[1],[1]]
        sol = Solution()
        self.assertEqual(-1, sol.orangesRotting(grid))


if __name__ == '__main__':
    unittest.main()
