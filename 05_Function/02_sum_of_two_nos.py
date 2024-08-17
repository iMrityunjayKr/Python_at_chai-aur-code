#Create a function that takes two numbers as parameters and return their sum.
print("Enter two no : ")
num1 = int(input("Num 1 : "))
num2 =  int(input( "Num 2 : "))
def sum_of_two_nos(num1,num2):
    return num1+num2
result = sum_of_two_nos(num1,num2)
print("The sum of ",num1, ",",num2, "is : ",result)