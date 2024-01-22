a = 7
b = 11
c = 3

largest = a
if largest < a:  # Note redundant statement
    largest = a
if largest < b:
    largest = b
if largest < c:
    largest = c

print(largest)
