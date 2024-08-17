#Factorial Calculator
#Find the factorial of a number using while loop.
number = int(input("Please enter a no for which, factorial to be calculated: "))
original_number = number;
factorial = 1


while number>0:
    factorial = factorial*number
    number = number -1
print("The factorial of number",original_number, "is : ",factorial)

