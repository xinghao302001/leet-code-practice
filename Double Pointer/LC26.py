## slow-fast pointer
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        slow = 0
        fast = 1

        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1

        return slow + 1
        
if __name__ == "__main__":
    test_case = [0,0,1,1,1,2,2,3,3,4]
    sol = Solution()
    res = sol.removeDuplicates(test_case)
    print(res)