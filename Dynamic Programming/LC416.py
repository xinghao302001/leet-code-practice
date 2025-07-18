from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        s //= 2
        n = len(nums)
        f = [[False] * (s + 1) for _ in range(n + 1)]
        f[0][0] = True
        for i, x in enumerate(nums):
            for j in range(s + 1):
                f[i + 1][j] = j >= x and f[i][j - x] or f[i][j]
        return f[n][s]
