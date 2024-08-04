def count_combinations(n):
    count = 0
    for p in range(1001):
        for q in range(1001):
            for r in range(1001):
                for s in range(1001):
                    if p + q + r + s == n:
                        count += 1
    return count

# Example: Find combinations for n = 10
n = 10
result = count_combinations(n)
print(f"Number of combinations for {n}: {result}")
