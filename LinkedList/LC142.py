## fast-slow pointer
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None


# Method 2 set
# class Solution:
#     def detectCycle(self, head: ListNode) -> ListNode:
#         visited = set()

#         while head:
#             if head in visited:
#                 return head
#             visited.add(head)
#             head = head.next

#         return None
