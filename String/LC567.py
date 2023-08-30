from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need, window = defaultdict(int), defaultdict(int)

        for c in s1:
            need[c] += 1
        
        left, right = 0,0
        valid = 0
         
        while right < len(s2):
            c = s2[right]
            right += 1

            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid+=1
            
            while right - left >= len(s1):
                if valid == len(need):
                    return True

                d = s2[left]
                left += 1

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return False
    
if __name__=="__main__":
    sol = Solution()
    ts_str_a = "DADOBECODEBANC"
    ts_str_b = "AB"
    res = sol.checkInclusion(ts_str_b, ts_str_a)
    print(res)
