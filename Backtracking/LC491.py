# Non-decreasing Subsequences

from typing import List

class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        self.backtracking(nums, 0)
        return self.res

    def backtracking(self, nums, startIndex):
        if len(self.path) >= 2:
            self.res.append(self.path[:])
        if startIndex == len(nums):
            return
        
        used_set = set()
        for i in range(startIndex, len(nums)):
            ### 
            if (self.path and nums[i] < self.path[-1]) or nums[i] in used_set:
                continue
            used_set.add(nums[i])
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()