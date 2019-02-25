# Sum of Square Numbers
print('Insert the number:')
n = input()
n = int(n)

sum1 = 0
for i in range(1, n):
    if n == sum1:
        print(True)
        break
    elif n > sum1:
        sum1 += i * i
    elif n < sum1:
        print(False)
        break
    else:
        pass




