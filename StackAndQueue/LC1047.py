class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ele in s:
            if stack and stack[-1] == ele:
                stack.pop()
            else:
                stack.append(ele)
        return "".join(stack)
