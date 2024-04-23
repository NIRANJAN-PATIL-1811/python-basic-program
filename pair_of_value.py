def find_pairs_with_sum(lst, target_sum):
    pairs = []
    seen = set()

    for num in lst:
        complement = target_sum - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)

    return pairs

# Example usage:
lst = [1, 2, 3, 4, 5, 6]
target_sum = 7
result = find_pairs_with_sum(lst, target_sum)
print("Pairs with sum", target_sum, "are:", result)
