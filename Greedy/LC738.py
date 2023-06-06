## Monotone Increasing Digits

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        str_num = list(str(n))

        for i in range(len(str_num)-1, 0 , -1):
            if int(str_num[i]) < int(str_num[i-1]):
                str_num[i-1] = str(int(str_num[i-1]) - 1)
                ## change to "9": start from position i to end
                str_num[i:] = '9' * (len(str_num) - i)

        return int("".join(str_num))