# Importing array module
import array

# Function to append items to array
def append_to_array(arr, iterable):
    for item in iterable:
        arr.append(item)

# Main function
def main():
    # Creating an empty array of integer type ('i')
    my_array = array.array('i')

    # Sample iterable (list in this case)
    my_list = [10, 20, 30, 40, 50]

    # Appending items from iterable to array
    append_to_array(my_array, my_list)

    # Printing the array
    print("Array after appending items:", my_array)

# Calling main function
if __name__ == "__main__":
    main()
