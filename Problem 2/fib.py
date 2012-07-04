"""
By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms.
"""

num = 4000000

def fib(num):
    L1 = [0,1]
    i = L1[-1]
    while i < num:
        L1.append(L1[-1]+L1[-2])
        i = L1[-1]
    L1.pop()
    L2 = []
    for j in L1:
        if j % 2 == 0:
            L2.append(j)
    return sum(L2)

print fib(num)
