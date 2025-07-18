# Jump Game
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i, cover in enumerate(nums):
            if i > farthest:
                return False
            farthest = max(farthest, i + cover)
        return True
