# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we build a dictionary to keep track of all the numbers in nums and their corresponding indices.
        numbers_dict = {}
        for i in range(len(nums)):
            n = nums[i]
            numbers_dict[n] = numbers_dict.get(n, [])
            numbers_dict[n].append(i)

        # loop through the list to find if (target - n) is also in the above built dict.
        for i in range(len(nums)):
            n = nums[i]
            complement = target - n
            if complement in numbers_dict:
                if n != complement:
                    return [i, numbers_dict[complement][0]]
                elif len(numbers_dict[complement]) > 1:
                    return numbers_dict[complement][:2]

        return []
