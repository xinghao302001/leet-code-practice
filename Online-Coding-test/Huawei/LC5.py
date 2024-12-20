class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     res = ""
    #     for i in range(len(s)):
    #         s1 = self.find(s, i, i)  # 以当前字符为中心的最长回文子串（假设长度为奇数）
    #         s2 = self.find(
    #             s, i, i + 1
    #         )  # 以当前字符和下一字符为中心的最长回文子串（假设长度为偶数）
    #         res = s1 if len(res) < len(s1) else res
    #         res = s2 if len(res) < len(s2) else res
    #     return res

    # def find(self, s, left, right):
    #     """找到串s中，以left、right为中心的最长回文串"""
    #     while left >= 0 and right < len(s) and s[left] == s[right]:
    #         left -= 1
    #         right += 1
    #     return s[left + 1 : right]

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        start, max_length = 0, 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_length:
                    start, max_length = l, r - l + 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_length:
                    start, max_length = l, r - l + 1
                l -= 1
                r += 1

        return s[start : start + max_length]
