import math

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
    Calculates and returns the nth triangular number n(n+1)//2

    Args:
        n: integer n

    Returns:
        The nth triangular integer
    """
    t = n*(n+1)//2  # // for integer division
    return t

def sumpower(n, k):
    """
    Calculates and returns the sum of n powers over the range 1 to n+1.

    Args:
        n: an integer for the end range n + 1
        k: an integer for the power of each i in range

    Returns:
        The sum of the k power of a range of numbers i from 1 to n+1
    """
    total = 0
    for i in range(1, n+1):
        total += i**k  # total = total + i**k is also equivalent
    return total

print("Question 1")
print("I will use a for loop for n in range 1 to 101 to calculate the sumupto \n"
      "and triangular number for each n and print them.")
for n in range(1, 101):
    print('n = ', n, 'S_n = ', sumupto(n), "T_n = ", triangular(n))

print("Question 2")
print("My conjecture is that the power sum of 1 to n + 1 is equivalent to the triangular value of n.")

print("Question 3")
print("I will calculate the sum of the triangular(n) and triangular(n-1) for the range 1-20 for n.")
for n in range(1, 20):
    sumT = triangular(n) + triangular(n-1)
    print(sumT)
print("My conjecture for the relationship between n, triangular(n), and triangular(n-1) is \n"
      "that the sum of the triangular(n) and triangular(n-1) for an integer n is n**2.")

print("Question 4")
print("The power sum of (2024, 5) is", sumpower(2024, 5))

print("Question 5")
print("sumpower(100, -2) computes the sum of the range of numbers from 1 to 100 + 1 to the -2 power. ")

print("Question 6")
print("The power sum of (500, -2) is", sumpower(500, -2))
print("The power sum of (5000, -2) is", sumpower(5000, -2))
print("The power sum of (50000, -2) is", sumpower(50000, -2))

print("(Pi**2)/6 is approximately", (math.pi**2)/6)

print("it is reasonable to assume the power sum of 1 to infinity to the power of -2 is (pi**2)/6 because as the \n "
      "power sum of n goes higher and higher, the closer it gets to this value.")
