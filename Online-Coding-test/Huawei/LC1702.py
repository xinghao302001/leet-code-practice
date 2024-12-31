## Greedy


class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        # 找到第一个 "0" 的索引
        first_zero_index = binary.find("0")
        if first_zero_index < 0:
            return binary
        cnt1 = binary.count("1", first_zero_index)  # 统计 binary[i:] 中 '1' 的个数

        return "1" * (len(binary) - 1 - cnt1) + "0" + "1" * cnt1
