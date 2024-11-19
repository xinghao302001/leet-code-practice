from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right, i = 0, len(nums) - 1, len(nums) - 1
        res = [float("inf")] * len(nums)
        while left <= right:
            if nums[left] ** 2 < nums[right] ** 2:
                res[i] = nums[right] ** 2
                right -= 1
            else:
                res[i] = nums[left] ** 2
                left += 1
            i -= 1
        return res
