from typing import List


class Solution:
    # def generateMatrix(self, n: int) -> List[List[int]]:
    #     nums = [[0] * n for _ in range(n)]
    #     startx, starty = 0, 0
    #     loop, mid = n // 2, n // 2
    #     count = 1

    #     for offset in range(1, loop + 1):
    #         for i in range(starty, n - offset):
    #             nums[startx][i] = count
    #             count += 1
    #         for i in range(startx, n - offset):
    #             nums[i][n - offset] = count
    #             count += 1
    #         for i in range(n - offset, starty, -1):
    #             nums[n - offset][i] = count
    #             count += 1
    #         for i in range(n - offset, startx, -1):
    #             nums[i][starty] = count
    #             count += 1

    #         startx += 1
    #         starty += 1

    #     if n % 2 != 0:
    #         nums[mid][mid] = count
    #     return nums
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n <= 0:
            return []

        matrix = [[0] * n for _ in range(n)]
        top, bottom, left, right = 0, n - 1, 0, n - 1
        num = 1
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1

            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1

            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

        return matrix
