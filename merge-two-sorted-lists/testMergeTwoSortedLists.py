import unittest
from mergeTwoSortedLists import Solution, ListNode


class TestMergeTwoSortedLists(unittest.TestCase):

    def test_case_1(self):
        '''
        Input: 1->2->4, 1->3->4
        Output: 1->1->2->3->4->4
        '''

        l1 = ListNode(1)
        l1.next = ListNode(2)
        l1.next.next = ListNode(4)

        l2 = ListNode(1)
        l2.next = ListNode(3)
        l2.next.next = ListNode(4)

        sol = Solution()
        l3 = sol.mergeTwoLists(l1, l2)
        expected_list = [1, 1, 2, 3, 4, 4]

        result_list = l3.dump()
        self.assertEqual(expected_list, result_list)

    def test_case_2(self):
        '''
        Input: 1, 3->4
        Output: 1->3->4
        '''

        l1 = ListNode(1)

        l2= ListNode(3)
        l2.next = ListNode(4)

        sol = Solution()
        l3 = sol.mergeTwoLists(l1, l2)
        expected_list = [1, 3, 4]

        result_list = l3.dump()
        self.assertEqual(expected_list, result_list)

    def test_case_3(self):
        '''
        Input: None, 3->4
        Output: 3->4
        '''

        l1 = None

        l2= ListNode(3)
        l2.next = ListNode(4)

        sol = Solution()
        l3 = sol.mergeTwoLists(l1, l2)
        expected_list = [3, 4]

        result_list = l3.dump()
        self.assertEqual(expected_list, result_list)

if __name__ == '__main__':
    unittest.main()
