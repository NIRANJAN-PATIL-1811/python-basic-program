import math

def calculate_sector_area(radius, angle, is_angle_in_degrees=True):
    if is_angle_in_degrees:
        angle = math.radians(angle)
    area = 0.5 * (radius ** 2) * angle
    return area

# Example usage:
radius = float(input("Enter the radius of the circle: "))
angle = float(input("Enter the angle of the sector: "))
angle_unit = input("Is the angle in degrees or radians? (Enter 'degrees' or 'radians'): ")

is_angle_in_degrees = angle_unit.lower() == 'degrees'

area = calculate_sector_area(radius, angle, is_angle_in_degrees)
print(f"The area of the sector is: {area:.2f}")
