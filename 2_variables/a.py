# Ceates space in memory for x
x = 7

print("A", x)
# Overrides the value of x
x = 4

print("B", x)

# Sets the value of x based on itself.
x = 2 * x
print("C", x)

print("Hmm... why isn't the value of x printing out properly:", "x")

print("Aha!", x)
