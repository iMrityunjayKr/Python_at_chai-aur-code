#Write a function to calculate and return the square of a number.
number = int(input("Enter a no: "))
def square(number):
    return number**2
result = square(number)   
print("The square of",number," is : ",result)
