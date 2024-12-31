## double pointer

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # 用于记录不等于 val 的元素个数
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # 将不等 val 的元素移动到前面
                k += 1
        return k
