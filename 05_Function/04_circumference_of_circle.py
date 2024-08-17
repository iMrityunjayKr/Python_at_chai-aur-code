#Create a function that return both the area and circumference of a circle given by its radius.
import math
def circle_stat(radius):
    area = math.pi * radius **2
    circumference =  2 * math.pi * radius
    return area, circumference
area,circumference = circle_stat(5)

print("The area of circle is : ",round(area,2)," and circumference of circle is : ",round(circumference,3))

