## Restore IP Addresses

from typing import List


class Solution:
    def __init__(self) -> None:
        self.result = []

    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12: return []
        self.backtracking(s, 0, 0)
        return self.result

    def backtracking(self, s: str, startIndex: int,  point_num: int) -> None:
        if point_num == 3:
            if self.is_valid(s, startIndex, len(s)-1):
                self.result.append(s[:])
            return 
        for i in range(startIndex, len(s)):
            if self.is_valid(s, startIndex, i):
                #### This process is important 
                s = s[:i+1] + "." + s[i+1:]
                self.backtracking(s, i+2, point_num+1)
                s = s[:i+1] + s[i+2:]
                ##########################
            else:
                break


    def is_valid(self, s: str, start: int, end: int) -> bool:
        if start > end:
            return False
        if s[start] == "0" and start != end:
            return False
        if not (0 <= int(s[start:end+1]) <= 255):
            return False
        return True