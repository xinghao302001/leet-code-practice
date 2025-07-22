## Combination
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        path = []

        def backtracking(n, k, startIndex):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(startIndex, n - (k - len(path)) + 2):
                path.append(i)
                backtracking(n, k, i + 1)
                path.pop()

        backtracking(n, k, 1)

        return res


# if __name__ == "__main__":
#     n=4
#     k=2
#     sol = Solution()
#     res = sol.combine(4,2)
#     print(res)
