# Palindrome Partitioning
from typing import List

class Solution:
    def __init__(self) -> None:
        self.res = []
        self.path = []

    def partition(self, s: str) -> List[List[str]]:
        self.backtracking(s, 0)
        return self.res

    def backtracking(self, s, startIndex):
        if startIndex >= len(s):
            self.res.append(self.path[:])
            return 

        for i in range(startIndex, len(s)):
            if(self.is_palindrome(s, startIndex, i)):
                ## left. right is closed
                self.path.append(s[startIndex:i+1])
                self.backtracking(s, i+1)
                self.path.pop()
            else:
                continue


    def is_palindrome(self, s, start, end) -> bool:
        i =  start
        j = end
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

