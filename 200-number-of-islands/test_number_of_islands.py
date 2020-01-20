import unittest
from number_of_islands import Solution, Solution2


class TestLC(unittest.TestCase):

    def test_case_1(self):
        grid = ['1 1 1 1 0'.split(), '1 1 0 1 0'.split(),
                '1 1 0 0 0'.split(), '0 0 0 0 0'.split()]
        sol = Solution()
        self.assertEqual(1, sol.numIslands(grid))

    def test_case_2(self):
        grid = ['1 1 0 0 0'.split(), '1 1 0 0 0'.split(),
                '0 0 1 0 0'.split(), '0 0 0 1 1'.split()]
        sol = Solution()
        self.assertEqual(3, sol.numIslands(grid))


class TestLC2(unittest.TestCase):

    def test_case_1(self):
        grid = ['1 1 1 1 0'.split(), 
                '1 1 0 1 0'.split(),
                '1 1 0 0 0'.split(), 
                '0 0 0 0 0'.split()]
        sol = Solution2()
        self.assertEqual(1, sol.numIslands(grid))

    def test_case_2(self):
        grid = ['1 1 0 0 0'.split(), '1 1 0 0 0'.split(),
                '0 0 1 0 0'.split(), '0 0 0 1 1'.split()]
        sol = Solution2()
        self.assertEqual(3, sol.numIslands(grid))

    def test_case_3(self):
        grid = [["1","1","1"],
                ["0","1","0"],
                ["1","1","1"]]
        sol = Solution2()
        self.assertEqual(1, sol.numIslands(grid))
        
    def test_case_4(self):
        grid = [["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]]
        sol = Solution2()
        self.assertEqual(3, sol.numIslands(grid))

if __name__ == '__main__':
    unittest.main()
