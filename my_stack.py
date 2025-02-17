from typing import Any, TypeVar, Optional

T = TypeVar('T')


class Node:
    def __init__(self, d: T):
        self.data = d
        self.next_node: Optional[T] = None


class Stack:
    def __init__(self):
        self.top: Optional[T] = None
        self.size = 0

    def push(self, d: T):
        new_node = Node(d)

        if self.top:
            new_node.next_node = self.top

        self.top = new_node
        self.size += 1


    def pop(self) -> T:
        if not self.top:
            return None

        r = self.top.data
        self.top = self.top.next_node
        self.size -= 1
        return r

    def peek(self):
        return self.top.data

    def is_empty(self) -> bool:
        return not bool(self.top)


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    stack.push(4)

    while not stack.is_empty():
        print(stack.peek())
        stack.pop()
