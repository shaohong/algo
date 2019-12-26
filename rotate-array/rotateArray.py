#ref: https://leetcode.com/problems/rotate-array/
from typing import List


class Solution:
    def _shift_right(self, nums: List[int]) -> None:
        '''
        right shift the array by 1 step
        '''
        if len(nums) <= 1:
            return None

        last_elem = nums[-1]
        for i in range(len(nums)-1, 0, -1):
            nums[i] = nums[i-1]
        nums[0] = last_elem

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            self._shift_right(nums)


class Solution2:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # save the last k elements
        if k >= len(nums):
            k = k % len(nums)

        if k == 0:
            return None

        last_k_elems = nums[-k:].copy()
        #print("last_k_elems", last_k_elems)
        # do the right shifting of k steps for elements at indices 0 ~ len(nums) -1 -k
        for i in range(len(nums)-k):
            nums[len(nums)-1 - i] = nums[len(nums)-1 - i - k]
        #print("shifting out right most k elems", nums)
        # copy the original last_k_elems to the front of the array
        for i, elem in enumerate(last_k_elems):
            nums[i] = elem


class Solution3:
    def reverseInList(self, nums: List[int], start: int, end: int) -> None:
        while(start < end):
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Approach #4 Using Reverse [Accepted]
        Algorithm

        This approach is based on the fact that when we rotate the array k times, 
        k elements from the back end of the array come to the front and the rest of the elements from the front shift backwards.

        In this approach, we firstly reverse all the elements of the array. 
        Then, reversing the first k elements followed by reversing the rest n-k elements gives us the required result.
        """

        k = k % len(nums)
        nums.reverse()
        self.reverseInList(nums, 0, k-1)
        self.reverseInList(nums, k, len(nums) - 1)
