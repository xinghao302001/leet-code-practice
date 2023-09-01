## ListNode
from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        p = dummy
        p1 = list1
        p2 = list2

        while p1 and p2:
            if p1.val > p2.val:
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next
        p = p.next

        if p1:
            p.next = p1
        if p2:
            p.next = p2

        return dummy.next
    


if __name__ == "__main__":
    list1 = [1,2,4]
    list2 = [1,3,4]
    sol = Solution()
    res = sol.mergeTwoLists(list1=list1, list2=list2)
    print(res)