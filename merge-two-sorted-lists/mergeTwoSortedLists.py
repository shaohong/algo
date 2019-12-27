# Ref: https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def length(self):
        count = 1
        next_node = self.next
        while next_node:
            next_node = next_node.next
            count += 1
        return count

    def dump(self) -> list:
        ret_list = [self.val]
        next_node = self.next
        while next_node:
            ret_list.append(next_node.val)
            next_node = next_node.next
        return ret_list


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if None in (l1, l2):
            return l1 or l2

        # initialize the result list, l3, to point to the head of l1 or l2
        l3_head = None  # the head of result list
        l3 = None  # the tail of result list
        next_node = None

        # walk through the two lists, do the merging
        while (l1 and l2):
            # find the next_node
            if l1.val < l2.val:
                next_node = l1
                l1 = l1.next
            else:
                next_node = l2
                l2 = l2.next

            # add the 'next_node' to l3
            if l3 == None:
                l3 = next_node
                l3_head = l3
            else:
                l3.next = next_node
                l3 = l3.next

        # deal with the left-over nodes
        l3.next = l1 or l2
        return l3_head

    #Ref: https://leetcode.com/problems/merge-two-sorted-lists/discuss/9735/Python-solutions-(iteratively-recursively-iteratively-in-place).

    def mergeTwoLists2(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists2(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists2(l1, l2.next)
            return l2
