# We fix the mistake in (b), by using type conversion!

x_as_string = "5"
x_as_number = int(x_as_string)

print("We have x=", x_as_number)
print("Double that is, ")
print(x_as_number * 2)
print(x_as_string * 2)
