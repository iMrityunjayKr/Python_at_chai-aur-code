#Write a funciton that greets a user. if no name is provide, it should greet with a default name.
def greet(name = "Mrityunjay"):
    return "Hello, " + name + "!"
print(greet())
print(greet("Hitesh"))
