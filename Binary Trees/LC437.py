from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        def dfs(node, curr_sum):
            if not node:
                return 0
            curr_sum += node.val
            count = prefix_sum[curr_sum - targetSum]
            prefix_sum[curr_sum] += 1

            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            ## backtrack: recover
            prefix_sum[curr_sum] -= 1
            return count

        return dfs(root, 0)
