## Find Bottom Left Tree Value
### Given the root of a binary tree, return the leftmost value in the last row of the tree.

from NodeDefinition import TreeNode
from typing import Optional

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        max_depth = -float("INF")
        leftmost_value = 0

        def __traverse(root, cur_depth):
            nonlocal max_depth, leftmost_value

            if not root.left  and not root.right:
                if cur_depth > max_depth:
                    max_depth = cur_depth
                    leftmost_value = root.val

            if root.left:
                __traverse(root.left, cur_depth + 1)
            if root.right:
                __traverse(root.right, cur_depth + 1)


        __traverse(root, 0)
        return leftmost_value