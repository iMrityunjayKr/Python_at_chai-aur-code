#Basic Class and Object.
#Create a Car class with attributes like brand and model.Then create an instance of this class.

class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        Car.total_car +=1
    def get_brand(self):
        return self.__brand + "!"
    def fuel_type(self):
        return "petrol or diesel"
    def full_name(self ):
        return f"{self.__brand} {self.__model}"
    @staticmethod
    def general_description():
        return "Cars are means of transport and are awesome."
    @property
    def model(self):
        return self.__model




class ElectricCar(Car):
    def __init__(self, __brand, __model, battery_size):
        super().__init__(__brand, __model)
        self.battery_size = battery_size

my_car = Car("Toyota", "Corolla")
# print(my_car.brand, my_car.model)


#Problem 2: Class Method and Self
#Add a Method to the Car class that displays the full name of the car (brand and model).

#implemented above.
# print(my_car.full_name())

#Problem 3: Inheritance
#Create an ElectricCar class that inherits the Car class and has an additional attribute battery_size
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric Charge"
#my_tesla = ElectricCar("Tesla", "Model S","85kwh")
# print(my_tesla.brand, my_tesla.model, my_tesla.battery_size)

# print(my_tesla.full_name())

#Problem 4: Encapsulation
#Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

# print(my_tesla.get_brand(),my_tesla.model)

#Problem 5: Polymorphism
#Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar but with different behaviours.

# safari = Car("Tata", "Safari")
# print(safari.fuel_type())
# print(my_tesla.fuel_type())

#Problem: 6: Class Variable
#Add a class variable to Car that keeps the track of the number of cars created.
Car("Tata","Nexon")
Car("Mahendra", "Thar")
# print(Car.total_car)

#Problem 7: Static Method
#Add a statci method to the Car that returns a general description of a car.

# we use @staticmethod  and here we don't need self.

print(my_car.general_description())
print(Car.general_description())

#Problem 8: Property Decorator
#Use a property decorator in the Car class to make the model attributes read-only.

# my_car.model = "city" # property is not letting this modify.

# print(my_car.model)

#Problem 9: Class Inheritance and isinstance() Fucntion
#Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.

my_tesla = ElectricCar("Tesla", "Model S","85kwh")

# print(isinstance(my_tesla,Car))

#Problem 10 : Multiple Instance
#Create two class Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine"

class ElectricCarTwo(Battery,Engine,Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")

# print(my_new_tesla.battery_info())
# print(my_new_tesla.engine_info())


