# Path Sum
## Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
#   A leaf is a node with no children.


from NodeDefinition import TreeNode
from typing import Optional

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def hasornot(root, targetSum) -> bool:
            if not root.left and not root.right and targetSum == 0:
                return True
            if not root.left and not root.right:
                return False
            
            if root.left:
                targetSum -= root.left.val
                if hasornot(root.left, targetSum):
                    return True
                targetSum += root.left.val
            if root.right:
                targetSum -= root.right.val
                if hasornot(root.right, targetSum):
                    return True
                targetSum += root.right.val
            
            return False
        
        if root == None:
            return False
        
        ## targetSum - root.val: for the situation -> tree only has one node
        else:
            return hasornot(root, targetSum - root.val)