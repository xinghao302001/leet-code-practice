# Maximize Sum Of Array After K Negations

from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums, key=abs, reverse=True)

        for i in range(len(sorted_nums)):
            if k > 0 and sorted_nums[i] < 0:
                sorted_nums[i] *= -1
                k -= 1
        while k > 0:
            sorted_nums[-1] *= -1
            k -= 1
        return sum(sorted_nums)

