# factorial program
num = int(input("enter a number"))
fact = 1
for i in range(1, num + 1):
    fact = fact * i
    if i == num:
        break
# print outside loop

print("Factorail of ", num, "is:", fact)
