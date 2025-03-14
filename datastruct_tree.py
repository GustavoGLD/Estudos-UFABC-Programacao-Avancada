from typing import TypeVar, Generic, Optional

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinaryTree(Generic[T]):
    def __init__(self, data: Optional[T] = None, node: Optional[Node[T]] = None):
        if node:
            self.root = node
        elif data:
            self.root = Node[T](data)
        else:
            self.root = None

    def height(self, node: Optional[Node[T]] = None) -> int:
        if node is None:
            node = self.root

        hleft = 0
        hright = 0

        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)

        if hright > hleft:
            return hright + 1
        else:
            return hleft + 1

    def print_in_order(self, node: Optional[Node[T]] = None):
        if not node:
            node = self.root
        if node.left:
            self.print_in_order(node.left)
        print(node.data)
        if node.right:
            self.print_in_order(node.right)

    def print_pre_order(self, node: Optional[Node[T]] = None):
        if not node:
            node = self.root
        print(node.data)
        if node.left:
            self.print_pre_order(node.left)
        if node.right:
            self.print_pre_order(node.right)

    def print_post_order(self, node: Optional[Node[T]] = None):
        if not node:
            node = self.root
        if node.left:
            self.print_post_order(node.left)
        if node.right:
            self.print_post_order(node.right)
        print(node.data)


if __name__ == '__main__':
    tree = BinaryTree[int](10)
    tree.root.left = Node(5)
    tree.root.right = Node(15)
    tree.root.left.left = Node(3)
    tree.root.left.right = Node(7)
    tree.root.right.left = Node(12)
    tree.root.right.right = Node(18)

    tree.print_post_order()
