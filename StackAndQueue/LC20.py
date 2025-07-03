# stack
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else "#"
                if top_element != mapping[char]:
                    return False
            else:
                stack.append(char)
        return not stack
