class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def peek(self):
        return self.head.data

    def enqueue(self, data):
        new_data = Node(data)
        if self.head is None:
            self.head = new_data
            self.tail = self.head
        else:
            self.tail.next = new_data
            self.tail = new_data

    def dequeue(self):
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return data
