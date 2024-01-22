hours_worked = float(input("How many hours did you work last week? "))
salary_hourly = float(input("How much do you earn per hour? "))

total_wage = hours_worked * salary_hourly

if total_wage >= 300:
    print("You are above the poverty line! ")
else:
    print("You are poor. ")
