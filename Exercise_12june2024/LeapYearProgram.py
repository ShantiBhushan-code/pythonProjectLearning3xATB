# Leap year program in python

year = int(input("Enter years: "))
if year % 4 == 0 and year % 100 != 0:
    print(year ," is Leap year")

elif year % 400 == 0:
    print(year, " is Leap year")

else:
    print(year, " is not Leap year")

