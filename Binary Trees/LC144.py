## preOrderTravesal
from NodeDefinition import TreeNode
from typing import List,Optional

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def travesal(root: TreeNode):
            if root == None:
                return 
            
            result.append(root.value)
            travesal(root.left)
            travesal(root.right)

        travesal(root)
        return result