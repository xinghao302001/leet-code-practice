## Combination Sum III
from typing import List

class Solution:
    def __init__(self):
        self.res = []
        self.cur_sum = 0
        self.path = []
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.backtracking(k, n, 1)
        return self.res

    def backtracking(self, k: int, n: int, startNum: int):
        if self.cur_sum > n:
            return
        
        if len(self.path) == k:
            if self.cur_sum == n:
                self.res.append(self.path[:])
            return
        
        for i in range(startNum, 9 - (k-len(self.path)) + 2):
            self.path.append(i)
            self.cur_sum += i
            self.backtracking(k, n, i+1)
            self.path.pop()
            self.cur_sum -= i
        

    