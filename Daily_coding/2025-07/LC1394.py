from typing import List
from collections import Counter


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq_arrs = Counter(arr)
        lucky_num = [num for num, count in freq_arrs.items() if num == count]
        return max(lucky_num) if lucky_num else -1
