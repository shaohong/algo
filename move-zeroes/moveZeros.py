# https://leetcode.com/problems/move-zeroes/
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        next_nonzero_place = 0
        i = 0

        # iterate through the array, if we find a non-zero element, add it after the 'last_nonzero_index'
        while i < len(nums):
            if nums[i] != 0:
                nums[next_nonzero_place] = nums[i]
                next_nonzero_place += 1
            i += 1

        # when we are done, all elements from(including) nums[next_nonzero_place] shall be 0
        for j in range(next_nonzero_place, len(nums)):
            nums[j] = 0
