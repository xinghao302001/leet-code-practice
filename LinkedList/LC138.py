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
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next

        # 第 2 步：处理 random 指针
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # 第 3 步：拆分链表
        curr = head
        new_head = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            curr = curr.next

        return new_head
