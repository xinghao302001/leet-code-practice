# Convert Sorted Array to Binary Search Tree


from NodeDefinition import TreeNode
from typing import List,Optional


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = self.traversal(nums, 0, len(nums)-1)
        return root


    def traversal(self, nums: List[int], left: int, right: int) -> TreeNode:
        if left > right:
            return None
        
        mid = left + (right - left) // 2

        root = TreeNode(nums[mid])

        root.left = self.traversal(nums, left, mid-1)
        root.right = self.traversal(nums, mid+1, right)

        return root
        