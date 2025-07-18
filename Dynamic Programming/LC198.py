from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        f0 = f1 = 0
        for i, num in enumerate(nums):
            new_f = max(f1, f0 + num)
            f0 = f1
            f1 = new_f
        return f1
