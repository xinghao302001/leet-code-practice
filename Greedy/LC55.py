# Jump Game
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0
        if len(nums) == 1:
            return True
        ## moving steps, i does not mean index
        ## i represents the index of cover range 
        i = 0
        while i <= cover:
            cover =  max(i + nums[i], cover)
            if cover >= len(nums) - 1:
                return True
            i += 1
        return False