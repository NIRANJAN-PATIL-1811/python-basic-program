import math

class Circle:
    def __init__(self, radius):
        """Initialize the Circle with a given radius."""
        self.radius = radius
    
    def get_radius(self):
        """Return the radius of the Circle."""
        return self.radius
    
    def set_radius(self, radius):
        """Set the radius of the Circle."""
        self.radius = radius
    
    def area(self):
        """Calculate and return the area of the Circle."""
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the Circle."""
        return 2 * math.pi * self.radius

# Example usage:
if __name__ == "__main__":
    # Create a Circle object with a radius of 5
    my_circle = Circle(5)
    
    # Print the area and perimeter of the circle
    print(f"Radius: {my_circle.get_radius()}")
    print(f"Area: {my_circle.area():.2f}")
    print(f"Perimeter: {my_circle.perimeter():.2f}")
    
    # Set a new radius and print the updated area and perimeter
    my_circle.set_radius(10)
    print(f"New Radius: {my_circle.get_radius()}")
    print(f"New Area: {my_circle.area():.2f}")
    print(f"New Perimeter: {my_circle.perimeter():.2f}")
