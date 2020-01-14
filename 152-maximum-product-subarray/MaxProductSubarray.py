# https://leetcode.com/problems/maximum-product-subarray/

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # using DP method:
        # DP state: DP[i] is the state of maximum product subarray decided at i-th position. 
        # DP[i][MAX] is the max and DP[i][MIN] is the minumum (e.g. a negative max).
        # DP transition equation:
        # DP[i][MAX] = max(DP[i-1][MAX]*nums[i], DP[i-1][MIN]*nums[i], nums[i])
        # DP[i][MIN] = min(DP[i-1][MAX]*nums[i], DP[i-1][MIN]*nums[i], nums[i])
        # as we iterate, we keep track of the max of DP[i][MAX]
        MAX=0
        MIN=1
        DP=[[nums[i], nums[i]] for i in range(len(nums))]
        CURR_MAX = nums[0]
        for i in range(1, len(nums)):
            DP[i][MAX] = max(DP[i-1][MAX]*nums[i], DP[i-1][MIN]*nums[i], nums[i])
            DP[i][MIN] = min(DP[i-1][MAX]*nums[i], DP[i-1][MIN]*nums[i], nums[i])
            CURR_MAX = max(DP[i][MAX], CURR_MAX)
            print(f"index {i}, {DP[i]}")
        return CURR_MAX
