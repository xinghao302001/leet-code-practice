# dp[i][j] 中的 i、j 表示前 i 个字符，不是索引！
# dp[i][0] = i -> word1 的前 i 个字符变成空串 => 删除 i 次
# dp[0][j] = j -> 空串变成 word2 的前 j 个字符 => 插入 j 次


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = (
                        min(
                            dp[i][j - 1],  # delete
                            dp[i - 1][j],  # insert
                            dp[i - 1][j - 1],  # replace
                        )
                        + 1
                    )
        return dp[-1][-1]
