# Partition Labels

from typing import List


# class Solution:
#     def partitionLabels(self, s: str) -> List[int]:
#         hash_map = [0] * 26
#         ## record the farest distance for each letter
#         for i in range(len(s)):
#             hash_map[ord(s[i]) - ord('a')] = i

#         result = []
#         left = 0
#         right = 0
#         for i in range(len(s)):
#             ## continuously update
#             right =  max(right, hash_map[ord(s[i]) - ord('a')])
#             if i == right:
#                 result.append(right - left + 1)
#                 ## update the lower bound of the next interval
#                 left = i + 1
#         return result


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {ch: i for i, ch in enumerate(s)}  # 记录每个字母最后一次出现的位置
        res = []
        start = end = 0

        for i, ch in enumerate(s):
            end = max(end, last[ch])  # 当前区间的最远边界
            if i == end:
                res.append(end - start + 1)  # 记录区间长度
                start = i + 1  # 开始下一个区间

        return res
