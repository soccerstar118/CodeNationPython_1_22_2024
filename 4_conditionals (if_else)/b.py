# Check if someone has enough money to go on a roller-coaster

money = float("How much money do you have? ")

if money > 500:
    height = float("How tall are you (in inches): ")

    if height > 48:
        print("You can go on the ride! ")
    else:
        print("You are too short to go on the ride. ")
else:
    print("You can't afford the ride")
