#Function with **kwargs
#Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.
# def print_kwargs(name, power):
#     print("Name",name, "Power : ",power)
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name= "Shaktiman", power = "lazer")
print_kwargs(name= "Shaktiman")
print_kwargs(name= "Shaktiman", power = "lazer",enemy = "Dr. jackaal")