# Center Diffusion
from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1 : r]

        res = ""
        for i in range(len(s)):
            s1 = palindrome(s, i, i)
            s2 = palindrome(s, i, i + 1)

            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2
        return res


"""
    def is_palindrome(self, s, start, end) -> bool:
        i =  start
        j = end
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True
"""
