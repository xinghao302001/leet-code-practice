from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        water_result = 0
        while left < right:
            if height[left] < height[right]:
                if (
                    height[left] >= left_max
                ):  # Update left_max if current height is greater, becuse it can trap water only if the current height is less than the max height seen so far.
                    left_max = height[left]
                else:
                    water_result += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    # Update right_max if current height is greater, because it can trap water only if the current height is less than the max height seen so far.
                    right_max = height[right]
                else:
                    water_result += right_max - height[right]
                right -= 1
        return water_result
