## Find K Closest Elements

from typing import List
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # the position that Bs finds
        p = self.left_bound(arr, x)
        left, right = p - 1, p
        res = []
        while right-left-1 < k:
            if left == -1:
                res.append(arr[right])
                right += 1
            elif right == len(arr):
                res.insert(0, arr[left])
                left -= 1
            elif x - arr[left] > arr[right] - x:
                res.append(arr[right])
                right += 1
            else:
                res.insert(0, arr[left])
                left -= 1
        return res

    def left_bound(self, nums:List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        
        return left