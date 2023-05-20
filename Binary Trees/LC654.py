# Maximum Binary Tree

from NodeDefinition import TreeNode
from typing import Optional, List


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        maxvalue = max(nums)
        index = nums.index(maxvalue)

        root = TreeNode(maxvalue)

        root_left = nums[:index]
        root_right = nums[index+1:]

        root.left = self.constructMaximumBinaryTree(root_left)
        root.right = self.constructMaximumBinaryTree(root_right)

        return root