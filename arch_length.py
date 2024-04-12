import math

def arc_length(radius, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    length = radius * angle_radians
    return length

radius = float(input("Enter the radius of the circle: "))
angle_degrees = float(input("Enter the angle in degrees: "))

length = arc_length(radius, angle_degrees)
print("The arc length is:", length)
