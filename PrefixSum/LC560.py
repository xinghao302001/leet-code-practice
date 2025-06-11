from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumCount = defaultdict(int)
        prefixSumCount[0] = 1

        count = 0
        preSum = 0

        for num in nums:
            preSum += num
            if preSum - k in prefixSumCount:
                count += prefixSumCount[preSum - k]
            prefixSumCount[preSum] += 1
        return count
