a = 23
b = -23

if a < 0:
    a = -a
if b < 0:
    b = -b

# don't like repetitive code - can define a function instead

def absolute_value(n):
    if n < 0:
        n = -n
        return n

def area(width, height):
    return width * height

"""Return the volume of a box given a width, length, and height."""
def volume(width, length, height):
    v = length * width * height
    return v

# function of volume has been defined
# values can now be put into defined function for output
# can return outputs and print things
# any variables inside the function is a local function only used to calculate function
    # cannot be called outside the function

# doc string can show what makes up function - also the help command on the function
# doc string required for function we have to write

# learned how to define functions and doc strings

# 1 on P3
def triangular(n):
    '''write doc string '''
    t = n*(n+1)//2 # // for integer division
    return t

# question 2 on p3
def sumupto(n):
    '''write doc string'''
    total = 0
    for i in range(1, n+1):
        total += i # total = total + i is also equivalent
        return total

# question 3 on p3
def sumpower(n, k):
    '''write doc string'''
    total = 0
    for i in range(1, n+1):
        total += i**k # total = total + i**7 is also equivalent
        return total

for n in range(1,101):
    print('n = ', n,'S_n = ', sumupto(n), "T_n = ", triangular(n))