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

    # def PreOrder(self):
    #     if self.key != 0:
    #         return self.key
    #         if self.left:
    #             (self.left).PreOrder()
    #         if self.right:
    #             (self.right).PreOrder()
# class PreOrder(BinaryTree):
#
#     def __init__(self, key):
#         self.key
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.key != 0:
#             yield self.key
#             if self.left:
#                 (self.left).__next__()
#             if self.right:
#                 (self.right).__next__()

    def PreOrder(self):
        if self.key != 0:
            print(self.key)
            if self.left:
                self.left.PreOrder()
            if self.right:
                self.right.PreOrder()

    def InOrder(self):
        if self.key:
            if self.left:
                self.left.InOrder()
            print(self.key)
            if self.right:
                self.right.InOrder()

    def PostOrder(self):
        if self.key:
            if self.left:
                self.left.PostOrder()
            if self.right:
                self.right.PostOrder()
            print(self.key)


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



