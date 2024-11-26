from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        cur = dummy_head
        while cur.next and cur.next.next:
            tmp = cur.next
            tmp_1 = cur.next.next.next

            cur.next = cur.next.next
            cur.next.next = tmp
            tmp.next = tmp_1
            cur = cur.next.next
        return dummy_head.next
