from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(left, right, path):
            if len(path) == 2 * n:
                res.append(path)
                return
            if left < n:
                backtrack(left + 1, right, path + "(")
            if right < left:
                backtrack(left, right + 1, path + ")")  ## string-backtrack

        backtrack(0, 0, "")
        return res
