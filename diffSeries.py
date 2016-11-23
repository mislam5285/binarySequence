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

def series(n,x,k,palindrome=False):
    if not palindrome:
        lengthSeries=[]
        for i in range(x,n+1):
             lengthSeries.append( len(func(i,x,k)))
        return lengthSeries
    else:
        lengthSeries=[]
        for i in range(x,n+1):
             lengthSeries.append( len(palindromic(i,x,k)))
        return lengthSeries

def diffSeries(series1):
    diffSerLen=[]
    for i in range(len(series1)-1):
        diffSerLen.append(series1[i+1]-series1[i])
    print diffSerLen
    return diffSerLen

def pattern(lengthSeries):
    size=len(lengthSeries)
    if (lengthSeries[size-1]-lengthSeries[size-2]>0):
        lengthSeries= diffSeries(lengthSeries)
        pattern(lengthSeries)




if __name__ == '__main__':
    x = 3
    k = 1
    n = 8           #upto n
    print "n=", n, "x=", x, "k=", k
    lengthSeries=series(n,x,k)
    print lengthSeries
    # pattern(lengthSeries)
    palindromeSeries=series(n,x,k,palindrome=True)
    print palindromeSeries
