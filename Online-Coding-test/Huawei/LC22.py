from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current: str, open_count: int, close_count: int):
            # 如果当前字符串的长度达到了 2 * n，则将其加入结果中
            if len(current) == 2 * n:
                result.append(current)
                return

            # 如果可以添加左括号，则递归地添加
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # 如果可以添加右括号，则递归地添加
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        # 从空字符串开始构建
        backtrack("", 0, 0)
        return result
