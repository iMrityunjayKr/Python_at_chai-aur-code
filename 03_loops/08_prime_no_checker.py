#check a no is prime or not
number = int(input("Enter a no to check, whether it is prime or not : "))
is_prime = True

if number>1:
    for i in range (2, number):
        if (number % i) ==0:
            is_prime = False
            break
if (is_prime):
    print("The number",number,"is a prime no.")
else:
    print("The number",number,"is not a prime no.")

