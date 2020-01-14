# Ref: https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List


class Solution:

    @staticmethod
    def _v2rIdx(arraySize, idx):
        return idx % arraySize

    @staticmethod
    def binarySearchWithVirtualIdx(a: List[int], low: int, high: int, target: int) -> int:
        while (low <= high):
            vmid = (low + high) // 2
            mid = Solution._v2rIdx(len(a), vmid)
            if a[mid] == target:
                return mid
            elif a[mid] < target:
                low = vmid + 1
            else:
                high = vmid - 1

        return -1

    def find_min_idx(self, nums):
        '''
        find the index of the min vlaue in the roated array
        '''
        low = 0
        if nums[0] > nums[-1]:  # array is roated. need to find the starting point of 'low'
            while low < len(nums) and nums[low] < nums[low+1]:
                low += 1
            low += 1
        return low

    def find_min_idx_2(self, A):
        '''
        find the index of the min vlaue in the roated array
        '''
        # ref: https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14425/Concise-O(log-N)-Binary-search-solution

        lo = 0
        hi = len(A)-1
        # find the index of the smallest value using binary search.
        # Loop will terminate since mid < hi, and lo or hi will shrink by at least 1.
        # Proof by contradiction that mid < hi: if mid==hi, then lo==hi and loop would have been terminated.
        while (lo < hi):
            mid = (lo+hi)//2
            if (A[mid] > A[hi]):
                lo = mid+1
            else:
                hi = mid
        return lo

    def search(self, nums: List[int], target: int) -> int:
        # find the pivot point so that we know how to make an offset of the array
        # so that it becomes, virtually, a sorted ascending array
        if not nums:
            return -1

        low = self.find_min_idx_2(nums)

        # run the binary search on the virtual index space
        # with low = offset +1, high = len(nums) + offset
        return Solution.binarySearchWithVirtualIdx(nums, low, len(nums) - 1 + low, target)

