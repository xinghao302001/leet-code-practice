from functools import cache
from math import inf, isqrt


@cache
def dfs(i: int, j: int) -> int:
    if i == 0:
        return inf if j else 0
    if j < i * i:
        return dfs(i - 1, j)
    return min(dfs(i - 1, j), dfs(i, j - i * i) + 1)


class Solution:
    def numSquares(self, n: int) -> int:
        return dfs(isqrt(n), n)


# ------ 1:1 cancel recursive
N = 10000
f = [[0] * (N + 1) for _ in range(isqrt(N) + 1)]
for i in range(1, len(f)):
    for j in range(N + 1):
        if j < i * i:
            f[i][j] = f[i - 1][j]
        else:
            f[i][j] = min(f[i - 1][j], f[i - 1][j - i * i] + 1)


class Solution2:
    def numSquares(self, n: int) -> int:
        return dfs(isqrt(n), n)


## -------- optimize storage
N = 10000
f = [0] + [inf] * N
for i in range(N + 1):
    for j in range(i * i, N + 1):
        f[j] = min(f[j], f[j - i * i] + 1)


class Solution3:
    def numSquares(self, n: int) -> int:
        return f[n]
