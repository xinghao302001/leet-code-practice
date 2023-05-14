# Path Sum
### Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths \
### where the sum of the node values in the path equals targetSum. Each path should be returned \ 
### as a list of the node values, not node references.

from NodeDefinition import TreeNode
from typing import Optional, List


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # record all paths
        result = [] 
        # record current path, which satisify the goal
        path = []

        def traversal(cur_node, rest):
            if not cur_node.left and not cur_node.right:
                if rest == 0:
                    result.append(path[:])
                return 

            if cur_node.left:
                path.append(cur_node.left.val)
                ## backtrack
                traversal(cur_node.left, rest - cur_node.left.val)
                path.pop()

            if cur_node.right:
                path.append(cur_node.right.val)
                traversal(cur_node.right, rest - cur_node.right.val)
                path.pop()

        if not root:
            return []
        path.append(root.val)
        traversal(root, targetSum-root.val)
        return result