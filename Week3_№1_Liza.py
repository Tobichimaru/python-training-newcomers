import itertools

class BinaryTree(object):

    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None

    def insert(self, node):
        if node.key < self.key:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node)

    def PreOrder(self):
        if self.key != 0:
            yield self.key
            if self.left:
                for item in self.left.PreOrder():
                    yield item
            if self.right:
                for item in self.right.PreOrder():
                    yield item


    def InOrder(self):
        if self.key:
            if self.left:
                for item in self.left.InOrder():
                    yield item
            yield self.key
            if self.right:
                for item in self.right.InOrder():
                    yield item


    def PostOrder(self):
        if self.key:
            if self.left:
                for item in self.left.PostOrder():
                    yield item
            if self.right:
                for item in self.right.PostOrder():
                    yield item
            yield self.key


if __name__ == "__main__":
    c = BinaryTree(5)
    c.insert(BinaryTree(8))
    c.insert(BinaryTree(4))
    c.insert(BinaryTree(2))
    c.insert(BinaryTree(6))
    c.insert(BinaryTree(15))

    d = BinaryTree(10)
    d.insert(BinaryTree(5))
    d.insert(BinaryTree(15))
    d.insert(BinaryTree(3))
    d.insert(BinaryTree(6))
    d.insert(BinaryTree(4))
    d.insert(BinaryTree(2))
    d.insert(BinaryTree(7))
    d.insert(BinaryTree(17))
    d.insert(BinaryTree(14))
    d.insert(BinaryTree(11))
    d.insert(BinaryTree(18))

    print('Pre-order: ')
    for i in d.PreOrder():
        print(i, end=' ')
    print('\nIn-order: ')
    for i in d.InOrder():
        print(i, end=' ')
    print('\nPost-order: ')
    for i in d.PostOrder():
        print(i, end=' ')



