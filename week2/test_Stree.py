import unittest
from binary_search_tree import STree
from binary_search_tree import STree2

class STreeTestCase(unittest.TestCase):

    def test(self):
        r1 = STree(3)
        r1.insert(STree(7))
        r1.insert(STree(1))
        r1.insert(STree(5))
        r1.insert(STree(8))

        r2 = STree2(3)
        r2.insert(STree2(7))
        r2.insert(STree2(1))
        r2.insert(STree2(5))
        r2.insert(STree2(8))

        a = []
        for i in r1:
            a.append(i)
        b = []
        for i in r2:
            b.append(i)

        s1 = [3, 1, 7, 5, 8]
        s2 = [1, 3, 5, 7, 8]
        self.assertEqual(a, s1)
        self.assertEqual(b, s2)


if __name__ == '__main__':
    unittest.main()
