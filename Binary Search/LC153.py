from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1  # 最小值在右侧
            else:
                right = mid  # 最小值在左侧（包含 mid）

        return nums[left]
