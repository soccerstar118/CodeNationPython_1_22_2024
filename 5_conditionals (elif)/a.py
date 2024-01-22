hours_worked = float(input("How many hours did you work last week? "))
salary_hourly = float(input("How much do you earn per hour? "))

total_wage = hours_worked * salary_hourly

if total_wage >= 100_000:
    print("You are rich!")
elif total_wage >= 2000:
    print("You are making (at or above) 6 figures! ")
elif total_wage >= 1000:
    print("You are making more money than the median American!")
elif total_wage >= 300:
    print("You are doing okay (economically at least)! ")
else:
    print("You are below the poverty line in the U.S. ")
