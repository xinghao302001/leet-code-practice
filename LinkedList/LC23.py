from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        from heapq import heappush, heappop

        dummy = ListNode(0)
        curr = dummy
        heap = []

        # 初始化堆
        for i, node in enumerate(lists):
            if node:
                heappush(
                    heap, (node.val, i, node)
                )  # 用 (val, index, node) 避免相同值比较失败

        while heap:
            val, i, node = heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heappush(heap, (node.next.val, i, node.next))

        return dummy.next
