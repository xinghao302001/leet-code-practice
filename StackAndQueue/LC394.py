class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        curr_num = 0
        curr_str = ""
        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)
            elif ch == "[":
                num_stack.append(curr_num)
                str_stack.append(curr_str)
                curr_num = 0
                curr_str = ""
            elif ch == "]":
                rep_time = num_stack.pop()
                prev_str = str_stack.pop()
                curr_str = prev_str + curr_str * rep_time
            else:
                curr_str += ch
        return curr_str
