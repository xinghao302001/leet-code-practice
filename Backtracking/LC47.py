# Permutations II
from typing import List

class Solution:
    def __init__(self) -> None:
        self.path = []
        self.res = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        used = [False] * len(nums)
        self.backtracking(nums, used)
        return self.res

    def backtracking(self, nums, used):
        if len(self.path) == len(nums):
            self.res.append(self.path[:])
        
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i-1] and used[i-1] == False:
                continue
            ### 
            if used[i] == True:
                continue
            used[i] = True
            self.path.append(nums[i])
            self.backtracking(nums, used)
            self.path.pop()
            used[i] = False