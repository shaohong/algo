#ref: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        prev_value = nums[0]
        # go through each element starting from index 1
        # if the element is bigger than 'prev_value', move to the next. Other wise, it is a duplicate that shall be removed.
        i = 1
        while i < len(nums):
            if nums[i] > prev_value:
                prev_value = nums[i]
                i += 1
            else: # handle duplicate
                del nums[i]
        return len(nums)