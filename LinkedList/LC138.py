from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        # 第 1 步：插入新节点
        curr = head
        while curr:
            curr.next = Node(curr.val, curr.next)
            curr = curr.next.next

        # 第 2 步：处理 random 指针
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # 第 3 步：遍历交错链表中的新链表节点
        curr = head.next
        while curr.next:
            curr.next = curr.next.next
            curr = curr.next
        return head.next
