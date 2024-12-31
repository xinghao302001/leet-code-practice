## Dynamic Programming

from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        max_len = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_len = max(max_len, dp[i][j])
        return max_len


nums1 = [1, 2, 3, 2, 1]
nums2 = [1, 1, 1, 4, 7]
result = Solution().findLength(nums1, nums2)
print("最长公共子数组的长度是:", result)
