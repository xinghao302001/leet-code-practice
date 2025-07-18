## Dp !!!
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        ans = 0

        for i in range(1, n):
            if s[i] == ")":
                if s[i - 1] == "(":
                    if i >= 2:
                        dp[i] = dp[i - 2] + 2
                    else:
                        dp[i] = 2
                else:  ## !!!
                    if i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == "(":
                        if i - dp[i - 1] - 2 > 0:
                            dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                        else:
                            dp[i] = dp[i - 1] + 2
                ans = max(ans, dp[i])
        return ans


## stack
class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        stack = []  ## todo list
        for i, c in enumerate(s):
            if stack and s[stack[-1]] == "(" and c == ")":
                stack.pop()
                if not stack:
                    ans = max(ans, i + 1)
                else:
                    ans = max(ans, i - stack[-1])
            else:
                stack.append(i)
        return ans
