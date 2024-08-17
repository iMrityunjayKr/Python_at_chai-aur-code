#Transportation Mode selection
#Problem: Choose a mode of transportation based on the distance (eg., <3km: walk, 3-15 km: bike, >15km : Car)
distance = int(input("Enter the distance to travel in km : "))
if distance<3:
    print("Walk this distance.")
elif distance<=15:
    print("Take a bike to cover this distance.")
else:
    print("Take the car to travel this distance.")
