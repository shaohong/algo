#Ref: https://leetcode.com/problems/majority-element/
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # brute force. go through the list and do the counting. (if counter goes > n/2 we can return alreay)
        counters = {}
        half = len(nums) // 2
        for n in nums:
            counters[n] = counters.get(n, 0) + 1
            if counters[n] > half:
                return n

        return -1


class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        # ref: https://time.geekbang.org/course/detail/130-42713
        # do a sorting, and then pick the guy in the middle!
        if len(nums) == 1:
            return nums[0]
        # calculate the half position
        half = (len(nums) + 1) // 2
        return sorted(nums)[half-1]
