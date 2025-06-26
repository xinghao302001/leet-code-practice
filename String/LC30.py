from typing import List
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_map = Counter(words)
        res = []

        for i in range(len(s) - total_len + 1):
            seen = []
            for j in range(0, total_len, word_len):
                word = s[i + j : i + j + word_len]
                seen.append(word)
            if Counter(seen) == word_map:
                res.append(i)
        return res
