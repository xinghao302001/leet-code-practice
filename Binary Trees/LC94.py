# inorderTravesal
from NodeDefinition import TreeNode
from typing import List,Optional


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root == None:
            return
        def traversal(root:TreeNode):
            if root == None:
                return 
            
            traversal(root.left)
            result.append(root.value)
            traversal(root.right)

        traversal(root)
        return result