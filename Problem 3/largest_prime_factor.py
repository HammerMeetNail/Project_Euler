"""
Find the largest prime factor of a composite number.
"""

num = 600851475143

def largest_prime_factor(num):
    i = 2
    while i**2 <= num:
        while num % i == 0: #Locates smallest and largest factors of num
            if num == 2 or i**2 == num:
                return num / i
            print 'i =', i
            num = num / i #Assigns largest factor to num
            print 'num =', num
        i += 1
    return num

print largest_prime_factor(num)
