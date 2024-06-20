num = int(input("Enter a number: "))
originalnum = num
sum = 0
numberofdigits = len(str(num))
while num > 0:
    digit = num % 10
    sum = sum + pow(digit, numberofdigits)
    num = int(num / 10)

    if sum == originalnum:
        print("Armstrong number")


else:
 print("Not an armst1rong number")
