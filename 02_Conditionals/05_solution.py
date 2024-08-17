#Weather acitivity suggestion
#Problem: Suggest an acitvity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman) 
weather =  input("Update your weather, here : ")
if weather == "Sunny":
    activity = "Go for a walk"
elif weather == "Rainy":
    activity = "Read a book"
elif weather == "Snowy":
    activity = "Build a snowman"
print("Do this activity today : ", activity)
