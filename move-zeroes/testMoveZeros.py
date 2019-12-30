import unittest

from moveZeros import Solution


class TestMoveZeros(unittest.TestCase):
    def test_case_1(self):
        '''
        Input: [0,1,0,3,12]
        Output: [1,3,12,0,0]
        '''

        test_list = [0, 1, 0, 3, 12]
        expected_list = [1, 3, 12, 0, 0]
        sol = Solution()
        sol.moveZeroes(test_list)
        self.assertSequenceEqual(test_list, expected_list)
        pass


if __name__ == '__main__':
    unittest.main()
