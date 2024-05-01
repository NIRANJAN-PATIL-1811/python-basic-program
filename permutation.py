from itertools import permutations

def generate_permutations(items):
    # Generate initial permutation
    perm = list(permutations(items))
    yield perm

    # Generate successive permutations
    while True:
        # Find the index of the first pair of adjacent elements that can be swapped
        swap_index = None
        for i in range(len(items) - 1):
            if perm[0][i] != perm[0][i + 1]:
                swap_index = i
                break

        # If no pair found, stop iteration
        if swap_index is None:
            break

        # Swap the adjacent elements
        perm[0][swap_index], perm[0][swap_index + 1] = perm[0][swap_index + 1], perm[0][swap_index]
        yield perm

# Example usage
n = int(input("Enter the number of items: "))
items = list(range(1, n + 1))

generator = generate_permutations(items)
for i, perm in enumerate(generator):
    print(f"Permutation {i + 1}: {perm[0]}")
    if i == 10:  # Limiting to first 10 permutations for demonstration
        break
