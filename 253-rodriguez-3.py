print("P3: Functions")

print("Question 1")


def sumupto(n):
    """write doc string"""
    total = 0
    for i in range(1, n+1):
        total += i  # total = total + i is also equivalent
        return total


def triangular(n):
    """write doc string """
    t = n*(n+1)//2  # // for integer division
    return t


for n in range(1, 101):
    print('n = ', n, 'S_n = ', sumupto(n), "T_n = ", triangular(n))
