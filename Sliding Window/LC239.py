from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # record index(maximum_value)
        result = []

        for i in range(len(nums)):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)

            if dq[0] <= i - k:
                dq.popleft()

            if i >= k - 1:
                result.append(nums[dq[0]])
        return result


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    res = sol.maxSlidingWindow(nums, k)
    print(res)
