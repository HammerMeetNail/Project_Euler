"""
Add all the natural numbers below one thousand that are multiples of 3 or 5.
"""

def addnum():
    x = 0
    for i in range(1,1000):
        if i % 3 == 0:
            x = x + i
        elif i % 5 == 0:
            x = x + i
    return x

print addnum()
