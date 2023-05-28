# Combination Sum II
from typing import List

class Solution:
    def __init__(self) -> None:
        self.res = []
        self.path = []
        self.used = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.used = [False] * len(candidates) 
        candidates.sort()
        self.backtracking(candidates, target, 0, 0)
        return self.res

    def backtracking(self, candidates, target, cur_sum, startIndex):
        if cur_sum == target:
            self.res.append(self.path[:])
            return
        
        for i in range(startIndex, len(candidates)):
            if cur_sum + candidates[i] > target:
                return
            if i > 0 and candidates[i] == candidates[i-1] and self.used[i-1]==False:
                continue

            cur_sum += candidates[i]
            self.path.append(candidates[i])
            self.used[i] = True
            self.backtracking(candidates, target, cur_sum, i+1)
            cur_sum -= candidates[i]
            self.path.pop()
            self.used[i] = False
