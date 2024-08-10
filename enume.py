from enum import Enum

# Define an Enum class
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Access a member of the Enum
color = Color.RED

# Display the member name and value
print(f"Member name: {color.name}")
print(f"Member value: {color.value}")
