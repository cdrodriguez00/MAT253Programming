import math

print("P4: More Functions and Lists")

def hailstone(n):
    """takes positive integer n as input and returns a list called hailstone sequence
    first value
    sequence terminates at 1
    function(n) if n is even, n = n/2
    if n is odd, n= 3n+1
    """
    collatz = [n]

    while n != 1:
        if n%2 == 0:
            n =  n//2
        elif n%2 != 0:
            n = 3*n+2

    return collatz



