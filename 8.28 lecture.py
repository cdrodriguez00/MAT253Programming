for i in range(2,10,3):
    print(i)

print('1')
for n in range(1,21):   # for loop over range 1-20
    s = n**2    # perfect square calculation
    print(s)

print('2')
for n in range(1,21):  # for loop over range 1-20
    s = n**2   # perfect square calculation
    last_digit = s % 10   # to get remainder
    print(last_digit)

    #2,3, 7, 8 don't show up

print('3')
dont_see = (2, 3, 7, 8)
print(dont_see)

# python knows negatation
1 in dont_see
print(1 in dont_see)
not 1 in dont_see
print(not 1 in dont_see)

print('4')
print('Beginning verification...')

print('Verification complete.')