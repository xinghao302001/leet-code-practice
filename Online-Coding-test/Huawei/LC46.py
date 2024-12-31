## back-tracking
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 进行结果像的实现
        result = []

        # 完成迭代的进阶表示法
        def backtrack(path: List[int], remaining: List[List[int]]):
            # 如果没有剩余元素，表明已完成一个全排列 (通过叶子节点回收结果， 返回到for循环)
            if not remaining:
                result.append(path)
                return
            # 迭代剩余元素
            for i in range(len(remaining)):
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i + 1 :])

        # 调用回车函数，以给实际数组
        backtrack([], nums)
        return result
