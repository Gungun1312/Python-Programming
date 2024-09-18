num1 = int(input("Please enter the first integer: "))
num2 = int(input("Please enter the second integer: "))
num3 = int(input("Please enter the third integer: "))
if (num1 > num2 and num1 > num3):
    print ("The first number is the maximum number...")
    print ("So the maximum number is", num1)
elif (num2 > num3):
    print ("The second highest max number...")
    print ("So the maximum number is", num2)
else:
    print ("The third number is the maximum number...")
    print ("So the maximum number is", num3)
print ("End of the program...")