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

