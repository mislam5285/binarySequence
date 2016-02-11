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


if __name__ == '__main__':
    x = 4
    k = 3
    n = 7
    print "n=", n, "x=", x, "k=", k
    print func(n, x, k)
