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
                if cur_cover != len(nums) - 1:
                    result += 1
                    cur_cover = next_cover
                    if cur_cover >= len(nums) - 1:
                        break

        return result


class Solution2:
    def jump(self, nums: List[int]) -> int:
        jumps = 0  ## 当前跳跃次数 1 1 2
        end = 0  ## 当前这一步能跳到的最远位置 2 2 4
        farthest = 0  ## 能跳到的最远位置（从起点算） 2 4 4

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == end:  # 表示当前已经走到了这次跳跃所能覆盖的最远位置了
                jumps += 1
                end = farthest
                if end >= len(nums) - 1:
                    break
        return jumps
