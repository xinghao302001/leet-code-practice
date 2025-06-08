## sliding Window
from collections import Counter


class Solution:
    ## t <=> p
    def findAnagrams(s: str, p: str):
        res = []
        p_count = Counter(p)
        window_count = Counter()
        left = 0
        for right in range(len(s)):
            window_count[s[right]] += 1
            if right - left + 1 > len(p):
                window_count[s[left]] -= 1
                if window_count[s[left]] == 0:
                    del window_count[s[left]]
                left += 1
            if window_count == p_count:
                res.append(left)
        return res


if __name__ == "__main__":
    sol = Solution()
    ts_str_a = "cbaebabacd"
    ts_str_b = "abc"
    res = sol.findAnagrams(ts_str_a, ts_str_b)
    print(res)
