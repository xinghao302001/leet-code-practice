# Permutations
from typing import List

class Solution:
    def __init__(self) -> None:
        self.res = []
        self.path = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        self.backtracking(nums, used)
        return self.res
        
    def backtracking(self, nums, used):
        if len(self.path) == len(nums):
            self.res.append(self.path[:])
            return
        for i in range(0, len(nums)):
            if used[i] == True:
                continue
            used[i] = True
            self.path.append(nums[i])
            self.backtracking(nums, used)
            self.path.pop()
            used[i] = False
                