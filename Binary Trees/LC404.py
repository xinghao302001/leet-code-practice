# Sum of Left Leaves
from NodeDefinition import TreeNode
from typing import Optional

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_left_sum_of_leaves = self.sumOfLeftLeaves(root.left)
        right_left_sum_of_leaves = self.sumOfLeftLeaves(root.right)

        cur_val = 0

        if root.left and not root.left.left and not root.left.right:
            cur_val = root.left.val
        
        return cur_val + left_left_sum_of_leaves + right_left_sum_of_leaves