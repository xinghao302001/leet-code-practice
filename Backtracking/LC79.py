from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def backtrack(r, c, idx):
            if idx == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if board[r][c] != word[idx]:
                return False

            tmp = board[r][c]
            board[r][c] = "#"

            found = (
                backtrack(r + 1, c, idx + 1)
                or backtrack(r - 1, c, idx + 1)
                or backtrack(r, c + 1, idx + 1)
                or backtrack(r, c - 1, idx + 1)
            )

            board[r][c] = tmp  # backtrack/rollback 在循环内恢复现场 而不是循环外
            return found

        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True
        return False
