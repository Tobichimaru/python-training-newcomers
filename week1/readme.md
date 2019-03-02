### Theory

#### Types and data structures

Questions: 
1. Create 2-dimensional list in python. What is the difference between 
```
A = [[0]*5]*5
B = [[0 for _ in range(5)] for _ in range(5)]
```
2. Suppose we have a tuple
```
a = ([], 'abc', 123)
```
Can I put this tuple into the set? 
```
C = set()
C.add(a)
```
3. What is the result of this code
```
tuple('abc')
```
4. Set a list object as a key in a dictionary, i.e. 
```
a = [1, 2, 3]
D = dict()
D[a] = 'some value'
```
5. What is the result of this code
```
from decimal import Decimal
from fractions import Fraction

D = dict()
D[1] = 'int'
D[1.0] = 'float'
D[1j] = 'complex'
D[Decimal(1)] = 'decimal'
D[Fraction(5, 5)] = 'fraction'
print(D)
```
6. What is the result of this code
```
a = 1
b = 1
print(a is b)
a = 1000
b = 1000
print(a is b)
```

#### Useful links: 

Types and collections:
1. Types in python3: https://docs.python.org/3/library/stdtypes.html
2. Playing with data types: https://github.com/Tobichimaru/Python/blob/master/Types%2C%20Intro.ipynb
3. String types: https://github.com/Tobichimaru/Python/blob/master/Strings%20Files%20and%20Bytes.ipynb
4. Collections: https://github.com/Tobichimaru/Python/blob/master/Collections.ipynb
5. Data models: https://docs.python.org/3/reference/datamodel.html

Clean code and testing:
1. Clean code, pep: https://github.com/Tobichimaru/Python/blob/master/Clean%20code.ipynb
2. Unit testing: https://github.com/Tobichimaru/Python/blob/master/Testing.ipynb
3. unittests framework doc: https://docs.python.org/3/library/unittest.html

**Additional materials:**
How dict works: https://habr.com/ru/post/247843/

**Note**: Feel free to use different material regarding data types and structures in Python.

tasks:
1. Implement your own class of Fraction with defined comparing operators (<, >, ==, etc), 
string representation ('str(frac_obj)'). This type should be hashable in order to be a key in a dict. 
Add simple unit testing for this class.

