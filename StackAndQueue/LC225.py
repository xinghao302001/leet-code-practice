# use Queue to implement stack
from collections import deque


class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        else:
            for i in range(len(self.queue) - 1):
                self.queue.append(self.queue.popleft())
            return self.queue.popleft()

    def top(self) -> int:
        if self.empty():
            return None
        else:
            for i in range(len(self.queue) - 1):
                self.queue.append(self.queue.popleft())
            tmp = self.queue.popleft()
            self.queue.append(tmp)
            return tmp

    def empty(self) -> bool:
        return not self.queue
