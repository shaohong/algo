import unittest
from removeDuplicate import Solution

class TestRemoveDuplicate(unittest.TestCase):

    def test_case_1(self):
        remove_duplicate_sol = Solution()
        test_list = [1,1,2]
        new_len = remove_duplicate_sol.removeDuplicates(test_list)
        expected_list=[1,2]
        self.assertEqual(expected_list, test_list[:new_len])


if __name__ == '__main__':
    unittest.main()