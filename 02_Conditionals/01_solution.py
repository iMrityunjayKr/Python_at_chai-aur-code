age = input("Enter your age : ")
age_in_int = int(age)
if age_in_int<13:
    print("You are a child")
elif age_in_int<20:
    print("You are a teenager")
elif age_in_int<60:
    print("You are an adult")
else:
    print("Welcome!, You are now senior citizen")
