import unittest
from mergeSortedArray import Solution2 as Solution

class TestMergeSortedArray(unittest.TestCase):

    def test_case_1(self):
        '''
        Input:
        nums1 = [1,2,3,0,0,0], m = 3
        nums2 = [2,5,6],       n = 3
        Output: [1,2,2,3,5,6]
        '''

        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3

        nums2 = [2, 5, 6]
        n = 3

        sol = Solution()
        sol.merge(nums1, m, nums2, n)
        expected_list = [1, 2, 2, 3, 5, 6]

        self.assertEqual(expected_list, nums1)

if __name__ == '__main__':
    unittest.main()
