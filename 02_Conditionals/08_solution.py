#Password Strength Checker
#Problem: Check if a password is "Weak", "Medium", "Strong". Criteria : <6 chars (weak), 6-10 chars (Medium), >10 (Strong).
password = input("Enter your password : ")
length = len(password)
if length<6:
    print("Weak Password")
elif length<10:
    print("Medium Password")
else:
    print("Strong Password")