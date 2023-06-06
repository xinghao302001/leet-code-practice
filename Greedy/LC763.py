# Partition Labels

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash_map = [0] * 26
        ## record the farest distance for each letter
        for i in range(len(s)):
            hash_map[ord(s[i]) - ord('a')] = i

        result = []
        left = 0
        right = 0
        for i in range(len(s)):
            ## continuously update
            right =  max(right, hash_map[ord(s[i]) - ord('a')])
            if i == right:
                result.append(right - left + 1)
                ## update the lower bound of the next interval
                left = i + 1
        return result
            
        