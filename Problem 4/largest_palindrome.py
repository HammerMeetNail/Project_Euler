"""
Find the largest palindrome made from the product of two 3-digit numbers.
"""

upper = 999*999
bottom = 100*100
L = []
L2 = []

def largest_palindrome():
    for e in range(bottom,upper): #Locates all palindromes
        e = str(e)
        if e[0] == e[-1] and e[1] == e[-2] and e[2] == e[-3]:
            e = int(e)
            L.append(e)
    for n in L: #Compiles list of all palindromes divisible by 3 digit integers
        for i in range(100,1000):
            if n % i == 0 and n/i > 99 and n/i < 1000 and n not in L2:
                L2.append(n)     
    return L2[-1]

print largest_palindrome()
