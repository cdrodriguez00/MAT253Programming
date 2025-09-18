print("P2: Sets")

print("Question 1")
A = {0, 1, 2, 3, 5, 10, 12}   # creating a set A
print("The Set for A is", A)
B = {2, 4, 6, 8, 10, 12, 14, 16}   # creating a set B
print("The Set for B is", B)
print("The set for A or B is", A | B)  # set A or set B
print("The set for A and B is", A & B)   # set A and set B
print("The set for A minus B is", A - B)   # set A minus B
print("The set for B minus A is", B - A)   # set B minus A

print("Question 2")
E = {2*n for n in range(0, 51)}   # creates a set E for all even numbers from 0 to 100
print("The set E is", E)

print("Question 3")
F = {n for n in range(101) if n % 2 == 0}   # # creates a set F for all even numbers from 0 to 100
print("The set F is", F)

print("Question 4")
print("Checking if E is a subset of F and if F is a subset of E")
print("Is set E equal to set F?")
print(E == F)
print("is set F equal to set E?")
print(F == E)

if (E == F) == (F == E):
    print("Sets E and F are the same set.")
