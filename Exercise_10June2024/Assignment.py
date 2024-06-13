# Python script to calculate  squre and cube of a number
num = int(input("Enter a number: "))
square = num ** 2
print(" Square of number is: ", square)
cube = num ** 3
print(" Cube of number is: ", cube)

# Take two number from input and print weather first
# number is grater , equeal or less than second number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print("First number is greater than second number")
elif num1 == num2:
    print("Both number are equal")
else:
    print("Second number is greater than first number")
