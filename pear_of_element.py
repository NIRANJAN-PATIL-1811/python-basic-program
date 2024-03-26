def find_pairs_with_sum(arr, target_sum):
    pairs = []
    seen = set()

    for num in arr:
        complement = target_sum - num
        if complement in seen:
            pairs.append((num, complement))
        seen.add(num)

    return pairs

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7]
target_sum = 8
pairs = find_pairs_with_sum(arr, target_sum)
if pairs:
    print("Pairs with sum", target_sum, ":", pairs)
else:
    print("No pairs found with sum", target_sum)
