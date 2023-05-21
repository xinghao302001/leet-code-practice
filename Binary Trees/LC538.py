# Convert BST to Greater Tree

from NodeDefinition import TreeNode
from typing import List,Optional



class Solution:
    def __init__(self) -> None:
        self.count = 0
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return
        
        self.convertBST(root.right)

        self.count += root.val
        root.val = self.count

        self.convertBST(root.left)

        return root
        

