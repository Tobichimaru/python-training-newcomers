c = int (input())
a = 1
b = 1
g = 0
while a <= c:
    for b in range(1, c):
         if a ** 2 + b ** 2 == c:
             g+=1
             break
         else:
             b = b + 1
    if g == 1:
        break
    a += 1

if  g == 0:
    print(False)
else:
    print(True)
