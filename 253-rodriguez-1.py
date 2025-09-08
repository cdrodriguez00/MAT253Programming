print("Question 1")
for n in range(1,21):   # for loop over range 1-20
    s = n**2    # perfect square calculation
    print(s, end=(", "))   #prints each perfect square on a single line

print("\nQuestion 2")
for n in range(1,21):  # for loop over range 1-20
    s = n**2   # perfect square calculation
    last_digit = s % 10   # to get remainder
    print(last_digit, end=(", "))   #prints all last digits in a single line

print("\nQuestion 3")
print("Based on the perfect squares that I have seen and their last digits,\n"
      "I believe that the numbers 2, 3, 7 and 8 will not show up in any \n"
      "positive perfect square.")

print("Question 4")
print("Beginning verification...")
for n in range(1, 10001): # for loop over range 1-10000
    s = n**2 # perfect square calculation
    last_digit = s % 10 # to get remainder
    conjectured_set = {2, 3, 7, 8} # set of numbers where conjecture is false if found
    if last_digit in conjectured_set:  # if the last digit is in the conjectured set
        print("Conjecture is false!") # conjecture is shown to be false
        break  # end the for loop if conjecture is shown to be false
print("Verification complete.") # for loop has finished running