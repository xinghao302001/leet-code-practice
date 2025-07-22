from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] - 1
                h_new = min(h, height[stack[-1]]) - height[top]
                res += distance * h_new
            stack.append(i)
        return res
