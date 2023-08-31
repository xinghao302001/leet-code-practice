from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        def removeElement(nums: List[int], val: int) -> int:
            pointer = 0
            for i in range(len(nums)):
                if nums[i] != val:
                    nums[pointer] = nums[i]
                    pointer += 1

            return pointer

        p = removeElement(nums, 0)
        for i in range(p, len(nums)):
            nums[i] = 0
        return nums

if __name__ == "__main__":
    test_case = [0,1,0,3,12]
    sol = Solution()
    res = sol.moveZeroes(test_case)
    print(res)