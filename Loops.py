nums = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# Write a loop that prints each of the numbers on a new line.
line1 = ""
for x in nums:
    line1 += str(x) + " "
print(line1)

# Write a second loop that prints each number and its square on a new line.
line2 = ""
for x in nums:
    line2 += "The square of " + str(x) + " is " + str(x*x) + " "
print(line2)
