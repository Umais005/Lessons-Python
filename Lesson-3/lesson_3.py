# Lesson 3

import math


base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print("The area of the triangle is:", area)

sd_a = float(input("Enter the length of side a: "))
sd_b = float(input("Enter the length of side b: "))
sd_c = float(input("Enter the length of side c: "))
perimeter = (sd_a + sd_b + sd_c)
print("The perimeter of the triangle is:", perimeter)

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print("The area of the rectangle is:", area)

m = 2
y_intercept = 2*0-2
x_intercept = (0+2)/m
print("The y-intercept of the line is:", y_intercept)
print("The x-intercept of the line is:", x_intercept)
print("The slope of the line is:", m)

x1 = 2
x2 = 6
y1 = 2
y2 = 10
slope = (y2 - y1) / (x2 - x1)
print("The slope of the line is:", slope)
e_distance = math.sqrt(((x2 - x1)**2 + (y2 - y1)**2))
print("The distance between the points is:", e_distance)

print("on" in "python" and "on" in "dragon")
print("jargon" in "I hope this course is not full of jargon")

wordlen = str(float(len("python")))
print(7//3 == int(2.7))
print(type("10") == type(10))
print(int(9.8) == 10)

hrs = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
pay = hrs*rate
print("Your weekly earning is:", pay)

years = int(input("Enter no. of years you have lived: "))
seconds = years*365*24*60*60
print("You have lived for", seconds, "seconds.")

for i in range(1, 6):
    print(f"{i} {i**0} {i**1} {i**2} {i**3}")
