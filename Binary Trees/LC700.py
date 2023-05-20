# Search in a Binary Search Tree

from NodeDefinition import TreeNode
from typing import Optional, List

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left)
        if root.val < val:
            return self.searchBST(root.right)
        
