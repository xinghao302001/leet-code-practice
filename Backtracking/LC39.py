# Combination Sum

from typing import List

class Solution:
    def __init__(self) -> None:
        self.path = []
        self.res = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # self.path.clear()
        # self.res.clear()
        candidates.sort()
        self.backtracking(candidates, target, 0, 0)
        return self.res

    def backtracking(self,candidates, target, cur_sum, startIndex) -> None:
        if cur_sum > target:
            return 
        if cur_sum == target:
            self.res.append(self.path[:])
            return

        for i in range(startIndex, len(candidates)):
            self.path.append(candidates[i])
            cur_sum += candidates[i]
            self.backtracking(candidates, target,cur_sum, i)
            cur_sum -= candidates[i]
            self.path.pop()