# Construct Binary Tree from Preorder and Inorder Traversal

### Given two integer arrays inorder and preorder where inorder is the inorder traversal of a binary ＼
###　tree and preorder is the preorder traversal of the same tree, construct and return the binary tree.
from NodeDefinition import TreeNode
from typing import Optional, List


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            if not preorder:
                  return
            
            root_val =  preorder[0]
            root = TreeNode(root_val)

            root_index =inorder.index(root_val)

            inorder_left = inorder[:root_index]
            inoder_right = inorder[root_index+1:]

            preorder_left = preorder[1:len(inorder_left)+1]
            preorder_right = preorder[1+len(inorder_left):]

            root.left = self.buildTree(preorder_left, inorder_left)
            root.right = self.buildTree(preorder_right, inoder_right)

            return root
