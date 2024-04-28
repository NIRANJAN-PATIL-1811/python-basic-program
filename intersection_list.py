def find_union_and_intersection(list1, list2):
    # Finding the union
    union = list(set(list1) | set(list2))
    
    # Finding the intersection
    intersection = list(set(list1) & set(list2))
    
    return union, intersection

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

union, intersection = find_union_and_intersection(list1, list2)
print("Union:", union)
print("Intersection:", intersection)
