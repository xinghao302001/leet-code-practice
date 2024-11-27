## sliding Window
from typing import List
from collections import defaultdict


class Solution:
    ## t <=> p
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need, window = defaultdict(int), defaultdict(int)

        for c in p:
            need[c] += 1

        left, right = 0, 0
        valid = 0
        res = []

        while right < len(s):
            c = s[right]
            right += 1

            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            # 判断左侧窗口是否要收缩
            while right - left >= len(p):
                # 当窗口符合条件时，把起始索引加入 res
                if valid == len(need):
                    res.append(left)
                d = s[left]
                left += 1

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return res


if __name__ == "__main__":
    sol = Solution()
    ts_str_a = "cbaebabacd"
    ts_str_b = "abc"
    res = sol.findAnagrams(ts_str_a, ts_str_b)
    print(res)
