# Construct Binary Tree from Preorder and Inorder Traversal

### Given two integer arrays inorder and preorder where inorder is the inorder traversal of a binary ＼
###　tree and preorder is the preorder traversal of the same tree, construct and return the binary tree.
from NodeDefinition import TreeNode
from typing import Optional, List


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)

        mid = inorder.index(root_val)

        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root
