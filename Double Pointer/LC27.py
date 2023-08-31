from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast = 0 
        slow = 0
        size = len(nums)
        while fast < size:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        return slow