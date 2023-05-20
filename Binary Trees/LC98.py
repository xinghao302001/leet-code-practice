# Validate Binary Search Tree

from NodeDefinition import TreeNode
from typing import Optional, List


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pre = None
        
        def __isValidBST(root: TreeNode) -> bool:
            nonlocal pre
            
            if not root:
                return True
            
            is_left_valid = __isValidBST(root.left)

            if pre and pre.val >= root.val: 
                return False
            ## !!
            pre = root

            is_right_valid = __isValidBST(root.right)
        
            return is_left_valid  and is_right_valid
        
        return __isValidBST(root)
            