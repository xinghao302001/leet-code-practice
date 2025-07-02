# Permutations
from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        used = [False] * len(nums)

        def backtrack(path: list[int]):
            if len(path) == n:
                res.append(path[:])
                return

            for i in range(n):
                if used[i]:
                    continue
                path.append(nums[i])
                ## !!!
                used[i] = True
                backtrack(path)
                path.pop()  ## !!
                used[i] = False

        backtrack([])  ## !!
        return res
