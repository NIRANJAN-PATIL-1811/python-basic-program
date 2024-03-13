import struct

def item_size(array_type):
    item = array_type()
    item_bytes = bytes(item)
    return len(item_bytes)

if __name__ == "__main__":
    array_type = input("Enter the type of array (e.g., 'i' for integer, 'f' for float): ")
    try:
        size = item_size(struct.Struct(array_type))
        print(f"Length in bytes of one array item in internal representation: {size} bytes")
    except struct.error as e:
        print("Error:", e)
