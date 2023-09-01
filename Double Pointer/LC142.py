## ListArray
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break  
        if not fast or not fast.next:
            return None
        slow = head
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return slow 