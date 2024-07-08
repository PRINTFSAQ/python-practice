day=int(input("enter the days = "))
year=int(day/365)
print("years =",year)

month=day%30
print("month =",month)

week=month%7
print("week = ",week)

days=week%7
print("days = ",days)