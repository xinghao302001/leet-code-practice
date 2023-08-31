### Sliding Window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window={}
        left, right = 0,0
        res = 0 
        while right < len(s):
            c = s[right]
            right += 1
            window[c] = window.get(c, 0) + 1

            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1
            
            res = max(res, right-left)
        return res
    

if __name__=="__main__":
    sol = Solution()
    ts_str = "abcdabcbb"
    res = sol.lengthOfLongestSubstring(ts_str)
    print(res)