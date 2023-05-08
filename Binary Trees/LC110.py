## balanced Binary Tree

# Recursive
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right =  right
        self.left = left


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if self.get_height(root) != -1:
            return True
        else:
            return False

    
    def get_height(self, root:TreeNode) -> int:
        if not root:
            return  0
        ## preOrdertravesal
        if (left_height := self.get_height(root.left)) == -1:
            return -1
        
        if (right_height := self.get_height(root.right)) == -1:
            return -1
        
        if abs(left_height - right_height > 1):
            return  -1 
        
        else:
            return 1 + max(left_height, right_height)