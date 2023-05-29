# Subsets II

from typing import List

class Solution:
    def __init__(self) -> None:
        self.res = []
        self.path = []
        self.used = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.used = [False] * len(nums)
        self.backtracking(nums, 0, self.used)
        return self.res

    def backtracking(self, nums, startIndex, used: List[bool]):
        self.res.append(self.path[:])
        
        for i in range(startIndex, len(nums)):
            if i>0 and nums[i-1] == nums[i] and self.used[i-1] == False:
                continue
            self.path.append(nums[i])
            self.used[i] = True
            self.backtracking(nums, i+1, used)
            self.path.pop()
            self.used[i] = False

        