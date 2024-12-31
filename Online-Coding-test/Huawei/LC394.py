## stack


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_str = ""
        cur_num = 0
        for ele in s:
            if ele.isdigit():
                cur_num = cur_num * 10 + int(ele)

            elif ele == "[":
                stack.append((cur_str, cur_num))
                cur_num = 0
                cur_str = ""

            elif ele == "]":
                last_string, repeat_num = stack.pop()
                cur_str = last_string + cur_str * repeat_num

            else:
                cur_str += ele

        return cur_str
