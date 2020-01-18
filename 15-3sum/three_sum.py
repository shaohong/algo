#Ref: https://leetcode.com/problems/3sum

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # ref: https://time.geekbang.org/course/detail/130-42705
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                # skip duplicate as this number already used as the first number
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:  # s == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    # skip the possible duplicates of nums[l] and nums[r]
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l, r = l+1, r-1
        return result


class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # ref: https://time.geekbang.org/course/detail/130-42705
        if len(nums) < 3:
            return []

        result = set()
        nums.sort()

        for i, v in enumerate(nums[:-2]):
            if i > 1 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-(v+x)] = 1  # put the expected complement in,
                else:  # I am the expected complement! Bingo!
                    result.add((v, -(v+x), x))

        return map(list, result)
