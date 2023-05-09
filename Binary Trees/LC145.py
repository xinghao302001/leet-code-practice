# postorderTravesal
from NodeDefinition import TreeNode
from typing import List,Optional


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def travesal(root: TreeNode):
            if root == None:
                return 
            
            
            travesal(root.left)
            travesal(root.right)
            result.append(root.val)

        travesal(root)
        return result