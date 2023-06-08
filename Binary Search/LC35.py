## Search Insert Position

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.left_bound(nums, target)

    def left_bound(self, nums: List[int], target: int) -> int: 
        if not nums:
            return -1
        
        left = 0
        right = len(nums) 

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                right = mid

        return left