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


print("Question 3")
for m in range(1, 20):
    sumT = triangular(m) + triangular(m-1)
    print(sumT)



print("Question 4")
def sumpower(n, k):
    """"write doc string"""
    total = 0
    for i in range(1, n+1):
        total += i**k  # total = total + i**7 is also equivalent
        return total

print(sumpower(100, 7))

print(sumpower(2024, 5))

print("Question 5")
print(sumpower(100, -2))

print("Question 6")
print(sumpower(500, -2))
print(sumpower(5000, -2))
print(sumpower(50000, -2))

