def divisors(n:int):
    count = 0
    for i in range(1, n+1):
        if n%i == 0:
            count += 1
    return count

"""
def divisors(n):
    return  len([l_div for l_div in range(1, n + 1) if n % l_div == 0]);

def divisors(n):
    return sum(1 for i in xrange(1, n + 1) if n % i == 0)

def divisors2(n):
    return sum([n % x == 0 for x in range(1, n + 1)])

def divisors(n):
    return sum(n%i==0 for i in range(1,n+1))
"""
