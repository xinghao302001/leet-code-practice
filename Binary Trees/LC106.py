# Construct Binary Tree from Inorder and Postorder Traversal

### Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary ＼
###　tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.
from NodeDefinition import TreeNode
from typing import Optional, List



class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return 
        
        root_val = postorder[-1]
        root = TreeNode(root_val)

        root_index = inorder.index(root_val)

        left_inorder= inorder[:root_index]
        right_inorder = inorder[root_index + 1 : ]

        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[len(left_inorder): len(postorder)-1]

        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)

        return root