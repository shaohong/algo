# Ref: https://leetcode.com/problems/merge-sorted-array/
from typing import List

'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
'''


class Solution1:

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        def shiftRight(nums, i):
            for x in range(len(nums)-1, i, -1):
                nums[x] = nums[x-1]
            pass

        # iterate through nums1 and nums2, pick the smaller one and add it to nums1, then adjust i, j:
        #   - if nums[i] was smaller, increase i, then
        #       - check if we're at the end of nums1 (i.e. i==j+m) and handle the situation
        #   - if nums[j] was smaller, insert nums[j] at position i, then increase i, then
        #       - check if we're at the end of nums2, i.e. j==n and handle the situation
        i, j = 0, 0
        while i < (j+m) and j < n:
            if nums1[i] < nums2[j]:
                i += 1
            else:
                shiftRight(nums1, i)
                nums1[i] = nums2[j]
                i += 1
                j += 1

        if i == j+m:
            # we reached end of nums1
            while (j < n):
                shiftRight(nums1, i)
                nums1[i] = nums2[j]
                i += 1
                j += 1
        else:
            # no need to do anything as things are in the right place
            pass


class Solution2:

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        Ref: https://leetcode.com/problems/merge-sorted-array/discuss/29503/Beautiful-Python-Solution
        """

        # iterate from tail to head, on both arrays, pick the bigger one and put it to nums1[k]

        # initialization
        i, j = m-1, n-1
        k = m + n - 1

        while i >= 0 and j >= 0:
            # find the bigger one and copy it to the final position.
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            # adjust the final position
            k -= 1

        # copy whatever left over from nums2
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
