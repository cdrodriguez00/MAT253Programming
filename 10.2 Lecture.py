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