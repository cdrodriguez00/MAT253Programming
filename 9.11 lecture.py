A = {3*x + 1 for x in range(1,101)}   #first term is 4 and last is 301
print(A) # in idle "A" in python shell should work

B= set()  # in idle "B" in python shell should print set()

for x in range(1,101):
    B.update({3*x +1})

# check B

# check A = B
# will print true

# if a not in B
print("3")
print ("Checking A is a subset of B.")
for a in A:
    (a in B)
    if not a in B:
        print("Something went wrong.", a, "is not in B.")
        break
print("check is done.")