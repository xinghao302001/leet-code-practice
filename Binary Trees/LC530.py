# Minimum Absolute Difference in BST

from NodeDefinition import TreeNode
from typing import Optional, List


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = []
        minVal = float("inf")

        def buildSortedList(root):
            if not root: return None
            if root.left:
                buildSortedList(root.left)
            
            res.append(root.val)

            if root.right:
                buildSortedList(root.right)
            
            return res

        buildSortedList(root)
        for  i in range(len(res)-1):
             minVal = min(abs(res[i]-res[i+1]), minVal)
        
        return minVal