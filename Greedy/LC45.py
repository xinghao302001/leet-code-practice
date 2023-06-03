# Jump Game II

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        cur_cover = 0
        next_cover = 0
        result = 0
        for i in range(len(nums)):
            next_cover = max(i + nums[i], next_cover)
            if i == cur_cover:
                ### if: cur_cover == index of length
                if cur_cover != len(nums) -1:
                    result += 1
                    cur_cover = next_cover
                    if cur_cover >= len(nums) -1:
                        break

        return result

