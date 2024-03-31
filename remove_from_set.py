# Sample set
my_set = {1, 2, 3, 4, 5}

# Function to remove an item from the set if it is present
def remove_item(set_name, item):
    if item in set_name:
        set_name.remove(item)
        print(f"Item {item} removed from the set.")
    else:
        print(f"Item {item} is not present in the set.")

# Example usage
item_to_remove = 3
remove_item(my_set, item_to_remove)
print("Updated set:", my_set)

item_to_remove = 6
remove_item(my_set, item_to_remove)
print("Updated set:", my_set)