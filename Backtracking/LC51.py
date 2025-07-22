# N-Queens

import enum
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if not n:
            return []

        board = [["."] * n for _ in range(n)]
        res = []

        def isValid(board, row, col):

            for i in range(len(board)):
                if board[i][col] == "Q":
                    return False

            i = row - 1
            j = col - 1

            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            i = row - 1
            j = col + 1

            while i >= 0 and j < len(board):
                if board[i][j] == "Q":
                    return False

                i -= 1
                j += 1

            return True

        def backtracking(board, row, n):
            if row == n:
                temp_res = []
                for temp in board:
                    temp_str = "".join(temp)
                    temp_res.append(temp_str)
                res.append(temp_res)

            for col in range(n):
                if not isValid(board, row, col):
                    continue

                board[row][col] = "Q"
                backtracking(board, row + 1, n)
                board[row][col] = "."

        backtracking(board, 0, n)
        return res


class Solution2:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        queens = [0] * n
        col = [False] * n
        diag1 = [False] * (n * 2 - 1)
        diag2 = [False] * (n * 2 - 1)

        def backtrack(r: int) -> None:  # r: row
            if r == n:
                ans.append(["." * c + "Q" + "." * (n - 1 - c) for c in queens])
                return

            for c, used in enumerate(col):  # c: col
                if not used and not diag1[r + c] and not diag2[r - c]:
                    queens[r] = c
                    col[c] = diag1[r + c] = diag2[r - c] = True
                    backtrack(r + 1)
                    col[c] = diag1[r + c] = diag2[r - c] = False

        backtrack(0)
        return ans
