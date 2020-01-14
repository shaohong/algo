# https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # use DP
        # DP states: let LIS[i] represent the length of longest increasing sequence that ends at nums[i]
        # DP state formula: LIS[i+1] = 1 + max(LIS[j] where j<i and nums[j]< nums[i])
        # result is the max of LIS list

        if not nums:
            return 0
        # initialization
        LIS = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            # find all the j where nums[j] < nums[i] (0<=j<i)
            LIS_PREV = []
            for j in range(i):
                if nums[j] < nums[i]:
                    LIS_PREV.append(LIS[j])
            if LIS_PREV:
                LIS[i] = 1 + max(LIS_PREV)

        return max(LIS)
