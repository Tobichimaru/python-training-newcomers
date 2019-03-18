class STree:
    def __init__(self, value, traversal):
        self.key = value
        self.left = None
        self.right = None
        self.traversal = traversal

    def __iter__(self):
        if self is None:
            raise StopIteration()
        if self.traversal == "inOrder":
            return self.in_order()
        elif self.traversal == "postOrder":
            return self.post_order()
        else:
            return self.pre_order()

    def pre_order(self):
        yield self.key
        if self.left is not None:
            for node in self.left:
                yield node
        if self.right is not None:
            for node in self.right:
                yield node

    def in_order(self):
        if self.left is not None:
            for node in self.left:
                yield node
        yield self.key
        if self.right is not None:
            for node in self.right:
                yield node

    def post_order(self):
        if self.left is not None:
            for node in self.left:
                yield node
        if self.right is not None:
            for node in self.right:
                yield node
        yield self.key

    def insert(self, value):
        if value < self.key:
            if self.left is None:
                self.left = STree(value, self.traversal)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = STree(value, self.traversal)
            else:
                self.right.insert(value)


if __name__ == "__main__":

    r1 = STree(3, "preOrder")
    r1.insert(7)
    r1.insert(1)
    r1.insert(5)
    r1.insert(8)

    print("PreOrderGenerator")
    for item in r1:
        print(item)

    r2 = STree(3, "inOrder")
    r2.insert(7)
    r2.insert(1)
    r2.insert(5)
    r2.insert(8)

    print("InOrderGenerator")
    for item in r2:
        print(item)

    r3 = STree(3, "postOrder")
    r3.insert(7)
    r3.insert(1)
    r3.insert(5)
    r3.insert(8)

    print("PostOrderGenerator")
    for item in r3:
        print(item)
