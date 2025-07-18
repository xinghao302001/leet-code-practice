## dp[i][j]=True: 表示：字符串 s[i..j] 是回文串


## s[i] == s[j]  AND  s[i+1..j-1] 是回文 ⇒ s[i..j] 是回文
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = s[0]
        for j in range(n):
            for i in range(0, j + 1):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    # update res
                    if j - i + 1 > len(res):
                        res = s[i : j + 1]
        return res
