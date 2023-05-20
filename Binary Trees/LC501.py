# Find Mode in Binary Search Tree

from NodeDefinition import TreeNode
from typing import Optional, List


class Solution:
    def __init__(self):
            self.pre = TreeNode()
            self.count = 0
            self.max_count = 0
            self.result = []
        
    def findMode(self, root: TreeNode) -> list[int]:
        if not root: return None
        self.search_BST(root)
        return self.result
        
    def search_BST(self, cur: TreeNode) -> List[int]:
        if not cur: return None
        self.search_BST(cur.left)

        if not self.pre:
             self.count += 1

        elif self.pre.val == cur.val:
             self.count += 1
        
        else: self.count = 1
        
        self.pre = cur
        if self.count == self.max_count:
             self.result.append(cur.val)
        if self.count > self.max_count:
             self.max_count = self.count
             self.result = [cur.val]
        
        self.search_BST(cur.right)
