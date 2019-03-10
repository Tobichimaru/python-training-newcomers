class STree:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None

    def __iter__(self):
        if self is None:
            raise StopIteration()
        yield self.key
        if self.left is not None:
            for node in self.left:
                yield node
        if self.right is not None:
            for node in self.right:
                yield node

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

"""class PreOrderIterator:
    def __init__(self, current):
        self._current = current
    def __iter__(self):
        return self._current.key
    def __next__(self):
        if self is None:
            raise StopIteration()
        for node in self._current.left:
            yield node.key
        for node in self._current.right:
            yield node.key"""

class STree2:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None

    def __iter__(self):
        if self is None:
            raise StopIteration()
        if self.left is not None:
            for node in self.left:
                yield node
        yield self.key
        if self.right is not None:
            for node in self.right:
                yield node

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

"""class InOrderIterator():
    def __init__(self, current):
        self._current = current
    def __iter__(self):
        return self._current.key
    def __next__(self):
        if self is None:
            raise StopIteration()
        for node in self._current.left:
            yield node.key
        for node in self._current.right:
            yield node.key"""

class STree3:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None

    def __iter__(self):
        if self is None:
            raise StopIteration()
        if self.left is not None:
            for node in self.left:
                yield node
        if self.right is not None:
            for node in self.right:
                yield node
        yield self.key

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

"""class PostOrderIterator():
    def __init__(self, current):
        self._current = current
    def __iter__(self):
        return self._current.key
    def __next__(self):
        if self is None:
            raise StopIteration()
        for node in self._current.left:
            yield node.key
        for node in self._current.right:
            yield node.key"""

if __name__ == "__main__":

    r1 = STree(3)
    r1.insert(STree(7))
    r1.insert(STree(1))
    r1.insert(STree(5))
    r1.insert(STree(8))

    print("PreOrderIterator")
    for item in r1:
        print(item)

    r2 = STree2(3)
    r2.insert(STree2(7))
    r2.insert(STree2(1))
    r2.insert(STree2(5))
    r2.insert(STree2(8))

    print("InOrderIterator")
    for item in r2:
        print(item)

    r3 = STree3(3)
    r3.insert(STree3(7))
    r3.insert(STree3(1))
    r3.insert(STree3(5))
    r3.insert(STree3(8))

    print("PostOrderIterator")
    for item in r3:
        print(item)

