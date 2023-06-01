##  Best Time to Buy and Sell Stock II
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(1, len(prices)):
            result += max(prices[i] - prices[i-1], 0)
        
        return result
        