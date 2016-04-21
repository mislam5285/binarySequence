__author__ = 'Prateek'
from itertools import product


def func(n, x, k):
    result = set()
    for suffix in product([1, 0], repeat=n):
        suffix = str(suffix).strip('(,)').replace(', ', '')
        if "0" * (k + 1) not in suffix:
            if "0" * k in suffix:
                if suffix.count('1') == (n - x):
                    result.add(suffix)
    return result


def funcLen(n, x, k):
    return func(n, x, k).__len__()


def cardinality(n, ):
    sum = 0
    for x in range(n + 1):
        for k in range(x + 1):
            sum = sum + funcLen(n, x, k)
    return sum

def perm(n,x):
    sum=0
    for k in range(x+1):
        sum=sum+funcLen(n,x,k)
    return sum

def noConsec(n):
    sum=1 #funcLen(n,0,0)
    for x in range(n+1):
        sum=sum+funcLen(n,x,1)
    return sum

if __author__ == 'Prateek':
    n=5
    k=2
    print cardinality(n)
    print noConsec(n), noConsec(n-1), noConsec(n-2)
    print perm(n,k)


