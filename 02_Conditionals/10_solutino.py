#Pet Food Recommendation 
#Problem: Recommend a type of pet food based on the pet's specis and age. (e.g., Dog: <2 year - Puppy food Cat : >5 years - Senior cat food.)
pet = input("Enter your pet species : ")
year_of_pet = int(input("Enter the year of your pet : "))
if pet== "Dog":
    if year_of_pet<2:
        print("Provide puppy food to the",pet)
    else:
        print("Provide adult food to the",pet)
elif pet == "Cat":
    if year_of_pet>5:
        print("Provide senior cat food to the",pet)
    else:
        print("Provide junior cat food to the",pet)