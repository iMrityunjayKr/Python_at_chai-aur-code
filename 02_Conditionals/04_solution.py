#Determine if a fruit is ripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)
fruit = input("Your fruit name please: ")
color = input("Tell me the color of your fruit: ")
if fruit == "Banana":
    if color == "Green":
        print("Your fruit is unripe")
    elif color == "Yellow":
        print("Your fruit is ripe")
    elif color == "Brown":
        print("Your fruit is overripe")
else:
    print("No information regarding your fruit")