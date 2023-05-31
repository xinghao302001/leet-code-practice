from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = - float("inf")
        count = 0 
        for i in range(len(nums)):
            count += nums[i]
            if count > res:
                res = count
            if count <= 0:
                count = 0
        return res