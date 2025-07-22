from collections import Counter
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        heap = []
        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num))  ## 比较的是元组的第一个元素
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]
