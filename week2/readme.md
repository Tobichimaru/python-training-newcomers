### Theory

#### Questions

##### Iterators
 
1. What is iterator?
2. What is an iterable collection?
3. What is a generator? 
4. Is generator - an iterator?
5. Is iterator - a generator? 

##### Data structures

1. What is HashTable? 
2. What is hash function? 
3. What methods of collision resolution do you know? 
4. How list is implemented in python? Is it a linked list or an array?

#### Useful links: 

1. Generators and iterators (theory): https://www.programiz.com/python-programming/generator
2. Iterators (theory): https://www.programiz.com/python-programming/iterator


#### Tasks:
1. Implement 3 iterators for binary search tree traversal: pre-order, post-order, in-order (https://en.wikipedia.org/wiki/Tree_traversal). You might define a tree like this:
```
class STree(object):
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None

def insert(r, node):
    if node.key < r.key:
        if r.left is None:
            r.left = node
        else:
            insert(r.left, node)
    else:
        if r.right is None:
            r.right = node
        else:
            insert(r.right, node)
```
Implement unit testing for these traversals. 

2. Implement a generator that returns odd numbers from 1 to defined `n`. 
