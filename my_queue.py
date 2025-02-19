from typing import TypeVar

T = TypeVar('T')


class Node:
    def __init__(self, data: T):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head: T = None
        self.tail: T = None

    def isEmpty(self) -> bool:
        return not bool(self.head)

    def peek(self) -> T:
        return self.head.data

    def enqueue(self, data: T) -> None:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def dequeue(self) -> T:
        data = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return data


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.dequeue()

while not queue.isEmpty():
    print(queue.dequeue(), end=' ')
