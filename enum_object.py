from enum import Enum

# Define an Enum class
class Weekdays(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

# Display a member name and value
def display_member(enum_member):
    print(f"Member name: {enum_member.name}")
    print(f"Member value: {enum_member.value}")

# Example usage
if __name__ == "__main__":
    # Display a member
    display_member(Weekdays.MONDAY)
