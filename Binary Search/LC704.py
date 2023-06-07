## Template for binary search

from typing import List

class Solution:
    ## case 1: basic case ---> find target
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while(left <= right):
            mid = left + (right -left) // 2 ## avoid int overflowing
            if (nums[mid] == target):
                return mid
            elif (nums[mid] > target):
                right = mid - 1
            elif (nums[mid] < target):
                left = mid + 1

        return -1
    
    ## Case 2: find target and find its lower bound
    def left_bound(nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while(left <= right):
            mid = left + (right-left) // 2
            if nums[mid] == target:
                right = mid -1
            elif nums[mid] > target:
                right = mid - 1
            elif  nums[mid] < target:
                left = mid + 1
        if left == len(nums):
            return -1
        return left if nums[left] == target else -1

    ## Case 3: find target and find its higher bound
    def right_bound(nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while(left <= right):
            mid = left + (right-left) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif  nums[mid] < target:
                left = mid + 1
        if left - 1 < 0:
            return -1
        return left-1 if nums[left-1] == target else -1