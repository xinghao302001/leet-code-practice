from typing import List

class Solution:
    def __init__(self):
        self.res: List[str] = []
        # self.path: str = []
        self.path: str = ""
        self.letter_map ={
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
    def letterCombinations(self, digits: str) -> List[str]:
        self.res.clear()
        if not digits: return []
        self.backtracking(digits, 0)
        return self.res
    
    def backtracking(self, digits: str, index: int) -> None:
        if index == len(digits):
            self.res.append(self.path)
            return 
        
        letters: str = self.letter_map[digits[index]]

        for letter in letters:
            # self.path.append(letter)
            self.path += letter
            self.backtracking(digits, index+1)
            # self.path.pop()
            self.path = self.path[:-1]
