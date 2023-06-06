# Binary Tree Cameras
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        """
        three states:
          0 ----> not covered
          1 ----> has camera
          2 ----> coverd
        """
        result = 0

        def traversal(curr: TreeNode) -> int:
            nonlocal result

            if not curr: return 2
            left = traversal(curr.left)
            right =  traversal(curr.right)

            ## case 1: left and right nodes are covered
            if left == 2 and right == 2:
                return 0
            
            ## case 2:
            ### At least one of the left node and the right node is covered
            elif left == 0 or right == 0:
                result += 1
                return 1
            
            ## case 3:
            ### At least one of the left node and the right node has camera
            elif left == 1 or right == 1:
                return 2
            
        if traversal(root) == 0:
            result += 1
        
        return result

        