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

def series(n,x,k):
    lengthSeries=[]
    for i in range(x,n+1):
         lengthSeries.append( len(func(i,x,k)))
    return lengthSeries

if __name__ == '__main__':
    x = 8
    k = 5
    n = 16           #upto n
    print "n=", n, "x=", x, "k=", k
    print series(n,x,k)
