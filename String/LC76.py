## sliding window !!!!
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, window = defaultdict(int), defaultdict(int)
        for c in t:
            need[c] += 1
        
        left, right = 0, 0
        valid = 0

        start, length = 0, float("inf")
        while right < len(s):
            c = s[right]
            right += 1

            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            
            while valid == len(need):
                if right - left < length:
                    start = left
                    length = right - left
                
                d = s[left]
                left += 1

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return "" if length == float("inf") else s[start:start+length]

if __name__=="__main__":
    sol = Solution()
    ts_str_a = "DADOBECODEBANC"
    ts_str_b = "ABC"
    res = sol.minWindow(ts_str_a, ts_str_b)
    print(res)    
