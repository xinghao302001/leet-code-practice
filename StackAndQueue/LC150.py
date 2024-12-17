## stack
from typing import List

from operator import add, sub, mul


def div(x, y):
    # 使用整数除法的向零取整方式
    return int(x / y) if x * y > 0 else -(abs(x) // abs(y))


class Solution:
    op_map = {"+": add, "-": sub, "*": mul, "/": div}

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in self.op_map:
                op1 = stack.pop()
                op2 = stack.pop()
                operation = self.op_map[token]
                stack.append(operation(op2, op1))
            else:
                stack.append(int(token))
        return stack.pop()
