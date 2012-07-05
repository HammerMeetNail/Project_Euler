"""
What is the smallest number divisible by each of the numbers 1 to 20?
"""

def small_div():
    check = 0
    i = 2520
    while check != 8:
        check = 0
        if i % 11 == 0 and i % 13 == 0 and i % 14 == 0 and i % 16 == 0:
            check += 4
        if i % 17 == 0 and i % 18 == 0 and i % 19 == 0 and i % 20 == 0:
            check += 4
        if check != 8:
            i += 20
    return i

print small_div()
