# Checking if someone has any reason to qualify for CodeNation extra points

extra_points = False

if input("Did homework? Enter y if yes [must be exact]: ") == "y":
    extra_points = True
if input("Did classwork? ") == "y":
    extra_points = True
if input("Went above and beyond in participation? ") == "y":
    extra_points = True

if extra_points:
    print("You get extra points! ")
else:
    print("You did not get any extra points D:")
