class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n <= 1:
            return False

        substr = ""
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                substr = s[:i]
                if substr * (n // i) == s:
                    return True

        return False
