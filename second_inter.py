def remove_intersection(first_set, second_set):
    intersection = first_set.intersection(second_set)
    return first_set - intersection

# Example usage:
if __name__ == "__main__":
    first_set = {1, 2, 3, 4, 5}
    second_set = {4, 5, 6, 7, 8}
    
    new_set = remove_intersection(first_set, second_set)
    print("First set after removing intersection:", new_set)
