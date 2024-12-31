## Backtracking


class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(position: int, visited: list[bool]):
            if position > n:
                return 1

            count = 0
            for num in range(1, n + 1):
                if not visited[num] and (num % position == 0 or position % num == 0):
                    visited[num] = True
                    count += backtrack(position + 1, visited)
                    visited[num] = False
            return count

        visited = [False] * (n + 1)

        return backtrack(1, visited)
