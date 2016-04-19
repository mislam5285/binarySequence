__author__ = 'Prateek'

from itertools import product

def func(n, x, k):
    result = set()
    for suffix in product([1, 0], repeat=n):
        suffix = str(suffix).strip('(,)').replace(', ', '')
        if "0" * (k + 1) in suffix:
            continue
        if "0" * (k) not in suffix:
            continue
        if suffix.count('1') == (n - x):
            result.add(suffix)
    return result.__len__()

def formula(n, x, k):
    sum = 0
    for i in range(0, k):
        sum = sum + func(n - i - 1, x - i, k)
    for j in range(0, k + 1):
        sum = sum + func(n - k - 1, x - k, j)
    # print "Using formula F(",n,',',x,',',k,') is',sum
    if sum == func(n, x, k):
        return True
    return False

if __author__ == 'Prateek':
    for n in range(1, 17):
        for x in range(n - 1):
            for k in range((n / n - x), x + 1):
                if formula(n, x, k) == False:
                    print n, x, k  # print values of n,x,k only if the result is incorrect
