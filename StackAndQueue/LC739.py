from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []  # todo list

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = (
                    stack.pop()
                )  # prev_index recodes corresponding position in ans.
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans
