#Leap Year Checker
#Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100) unless also divisible by 400.
year = int(input("Enter year to check whether it is leap year or not : "))
if year%4==0 and year%100!=0:
    print(year , ": is a leap year")
elif year% 400 ==0:
    print(year , ": is a leap year")
else:
    print("Entered year is not a leap year")
