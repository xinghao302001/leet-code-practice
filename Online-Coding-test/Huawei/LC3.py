class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur, res = [], 0
        for i in range(len(s)):
            while s[i] in cur:
                cur.pop(0)
            cur.append(s[i])
            res = max(len(cur), res)
        return res
