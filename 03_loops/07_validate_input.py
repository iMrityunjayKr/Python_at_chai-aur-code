#Validate input
# Problem: keep asking the user for input until they enter a number between 1 and 10.
#assuming, user will always give number in input.
while True:
    number = int(input("Enter a value between 1 to 10 : "))
    if 1<= number <=10:
        print("Thanks")
        break
    else:
        print("Invalid number, try again")


