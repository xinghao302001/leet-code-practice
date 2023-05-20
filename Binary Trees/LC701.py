# Insert into a Binary Search Tree

from NodeDefinition import TreeNode
from typing import Optional, List


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:


        if not root: return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)

        
        return root

        
             
         