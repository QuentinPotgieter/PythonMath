#python 33361908_Practical_5.py
#import math
import math
import statistics

#Assignment 1
print("Assignment 1\n")

value1 = float(input("Enter value 1: "))
value2 = float(input("Enter value 2: "))
value3 = float(input("Enter value 3: "))
value4 = float(input("Enter value 4: "))
value5 = float(input("Enter value 5: "))

data = [value1, value2, value3, value4, value5]

print("\nThe average of the values is: ", statistics.mean(data))

#Assignment 2
print("\nAssignment 2\n")

radius = float(input("What is the radius of the circle?: "))

Pi = math.pi
diameter = 2 * radius
circumference = round(2 * Pi * radius, 2)
area = round(Pi * radius * radius, 2)

print("\nThe radius of the circle is: " + str(radius))
print("The diameter of the circle is: " + str(diameter))
print("The circumference of the circle is: " + str(circumference))
print("The area of the circle is: " + str(area))

#Assignment 3
print("\nAssignment 3\n")

coordinateX1 = float(input("Enter coordinate 1 for point X: "))
coordinateX2 = float(input("Enter coordinate 2 for point X: "))
coordinateY1 = float(input("Enter coordinate 1 for point Y: "))
coordinateY2 = float(input("Enter coordinate 2 for point Y: "))

distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip((coordinateX1,coordinateX2), (coordinateY1,coordinateY2))]))

print("The distance between point1 and point 2 is: " + str(distance))
