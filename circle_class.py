import math

class Circle:
    def __init__(self, radius):
        """Initialize the circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius

    def __str__(self):
        """Return a string representation of the circle."""
        return f"Circle with radius {self.radius:.2f}"

# Example usage:
if __name__ == "__main__":
    # Create a circle with radius 5
    circle = Circle(5)
    
    # Print the area and perimeter of the circle
    print(f"Area: {circle.area():.2f}")
    print(f"Perimeter: {circle.perimeter():.2f}")
    print(circle)
