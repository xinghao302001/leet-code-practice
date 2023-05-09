##!! levelorderTravesal
from typing import Optional, List
from NodeDefinition import TreeNode

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = []
        if not root:
            return results
        from collections import deque

        que = deque([root])
        while que:
            size = len(que)
            result = []
            for _ in range(size):
                cur = que.popleft()
                result.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            
            results.append(result)

        return results


