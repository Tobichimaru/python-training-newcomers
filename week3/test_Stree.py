import unittest
from BSTGenerator import STree

class STreeTestCase(unittest.TestCase):

    def test(self):
        r1 = STree(3, "preOrder")
        r1.insert(7)
        r1.insert(1)
        r1.insert(5)
        r1.insert(8)

        r2 = STree(3, "inOrder")
        r2.insert(7)
        r2.insert(1)
        r2.insert(5)
        r2.insert(8)

        r3 = STree(3, "postOrder")
        r3.insert(7)
        r3.insert(1)
        r3.insert(5)
        r3.insert(8)

        a = []
        for i in r1:
            a.append(i)
        b = []
        for i in r2:
            b.append(i)
        c = []
        for i in r3:
            c.append(i)

        s1 = [3, 1, 7, 5, 8]
        s2 = [1, 3, 5, 7, 8]
        s3 = [1, 5, 8, 7, 3]
        self.assertEqual(a, s1)
        self.assertEqual(b, s2)
        self.assertEqual(c, s3)


if __name__ == '__main__':
    unittest.main()
