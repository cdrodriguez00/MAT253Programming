import math

print("P4: More Functions and Lists")

def hailstone(n):
    """takes positive integer n as input and returns a list called hailstone sequence
    first value
    sequence terminates at 1
    function(n) if n is even, n = n/2
    if n is odd, n= 3n+1
    collatz as name of sequence
    """
    collatz = [n]

    while n != 1:
        if n%2 == 0:
            n =  n//2
        elif n%2 != 0:
            n = 3*n+2
    collatz.append(n)
    return collatz

print("Problem 1")
print("Compute the hailstone sequence for 1")
hailstone(1)

print("Problem 2")
print("Compute the hailstone sequence for 27")
hailstone(27)


print("Problem 3")
print("Which positive integer n <= 20,000 has the longest hailstone sequence? How long is the /n"
      "hailstone sequence of this integer?")



