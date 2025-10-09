print("P3: Functions")

def sumupto(n):
    """
    Calculates the sum of a range of numbers

    Args:
        n: a positive integer n

    Returns:
        The sum of numbers in the range 1 to n + 1.
    """
    total = 0
    for i in range(1, n + 1):
        total += i  # total = total + i is also equivalent
    return total


def triangular(n):
    """
    Calculates and returns the nth triangularr number
    :param n:
    :return:
    """
    t = n*(n+1)//2  # // for integer division
    return t

def sumpower(n, k):
    """"write doc string"""
    total = 0
    for i in range(1, n+1):
        total += i**k  # total = total + i**k is also equivalent
    return total

print("Question 1")

for n in range(1, 101):
    print('n = ', n, 'S_n = ', sumupto(n), "T_n = ", triangular(n))


print("Question 3")
for m in range(1, 20):
    sumT = triangular(m) + triangular(m-1)
    print(sumT)



print("Question 4")

print("the sumpower of (100,7) is", sumpower(100, 7))

print(sumpower(2024, 5))

print("Question 5")

print(sumpower(100, -2))

print("Question 6")
print(sumpower(500, -2))
print(sumpower(5000, -2))
print(sumpower(50000, -2))

