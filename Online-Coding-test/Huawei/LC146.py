## double direction pointer
## double [dummy] nodes, head and tail


class Node:
    __slots__ = "prev", "next", "key", "value"

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.value = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            ## update value
            node = self.cache[key]
            node.val = value
            ## move to head
            self._move_to_head(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_head(node)
            self.size += 1
            if self.size > self.capacity:
                node = self._remove_tail()
                self.cache.pop(node.key)
                self.size -= 1

    def _move_to_head(self, node: Node):
        self._remove_node(node)
        self._add_to_head(node)

    def _remove_node(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_head(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node

    def _remove_tail(self):
        node = self.tail.prev
        self._remove_node(node)
        return node
