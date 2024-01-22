# Swapping 2 2_variables example
x = 100
y = 1
print("(x, y): ", x, y)
temp = x
y = x
x = temp
print("new (x, y): ", x, y)

# Note what happens without setting a temporary variable
a = 1
b = 2
print("(a,b): ", a, b)
a = b
b = a
print("new (a,b): ", a, b)
