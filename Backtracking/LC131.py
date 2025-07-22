# Palindrome Partitioning
## subset
from typing import List


class Solution:

    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)

        def backtrack(start, path):
            if start == n:
                ans.append(path[:])
                return ans
            for end in range(start + 1, n + 1):
                substr = s[start:end]
                if substr == substr[::-1]:
                    path.append(substr)
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])
        return ans
