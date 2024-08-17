#Assing a letter grade based on a student's score: A(90-100), B(80-89), C(70-79), D(60-69), E(below 60)
score = int(input("Enter your score obtained : "))
if score>=101:
    print("Please check you score again!")
    exit()
if score>=90:
    grade = 'A'
elif score>=80:
    grade = 'B'
elif score>=70:
    grade = 'C'
elif score>=60:
    grade = 'D'
else:
    grade = 'E'
print("Grade : ",grade)
