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

def palindromic(n,x,k):
    result=set()
    numbers=func(n=n,x=x,k=k)
    for number in numbers:
        if number==number[::-1]:
            result.add(number)
    return result

if __name__ == '__main__':
    x = 2
    k = 1
    n = 6
    print "n=", n, "x=", x, "k=", k
    print func(n, x, k)
    print palindromic(n, x, k)