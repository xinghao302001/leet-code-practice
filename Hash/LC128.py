from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0
        for num in num_set:
            if num - 1 not in num_set:
                cur = num
                cur_length = 1
                while cur + 1 in num_set:
                    cur += 1
                    cur_length += 1
                max_length = max(cur_length, max_length)
        return max_length
