# Look back at conditionals (c)

homework = input("Did homework? Enter y if yes [must be exact]: ")
classwork = input("Did classwork? ")
participated = input("Went above and beyond in participation? ")

if homework == "y" or classwork == "y" or participated == "y":
    print("Nice! You get more points. ")
else:
    print("You did not get any extra points D:")
