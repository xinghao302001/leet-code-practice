from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)

        sorted_elements = sorted(
            freq_map.keys(), key=lambda x: freq_map[x], reverse=True
        )

        return sorted_elements[:k]


# from collections import Counter
# import heapq


# def topKFrequent(nums, k):
#     # Step 1: Count the frequency of each element
#     freq_map = Counter(nums)

#     # Step 2: Use a heap to get the k most frequent elements
#     # We use a max-heap, so we pass negative frequency as the sorting key
#     top_k = heapq.nlargest(k, freq_map.keys(), key=lambda x: freq_map[x])

#     return top_k
