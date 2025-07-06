# Find First and Last Position of Element in Sorted Arrays
from typing import List

# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         return [self.left_bound(nums, target), self.right_bound(nums, target)]

#     def left_bound(self, nums: List[int], target: int) -> List[int]:
#         left = 0
#         right =  len(nums) - 1

#         while left <= right:
#             mid = left + (right - left) // 2
#             if nums[mid] < target:
#                 left = mid + 1
#             elif nums[mid] > target:
#                 right = mid - 1
#             elif nums[mid] == target:
#                 right = mid - 1

#         # check the situation when it is out of boundary
#         if left >= len(nums) or nums[left] != target:
#             return -1
#         return left

#     def right_bound(self, nums: List[int], target: int) -> List[int]:
#         left = 0
#         right = len(nums) - 1
#         while left <= right:
#             mid = left + (right - left) // 2
#             if nums[mid] < target:
#                 left = mid + 1
#             elif nums[mid] > target:
#                 right =  mid - 1
#             elif nums[mid] == target:
#                 left = mid + 1

#         if right < 0 or nums[right] != target:
#             return -1
#         return right


class Solution:

    def lower_bound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.lower_bound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = self.lower_bound(nums, target + 1) - 1
        return [start, end]
