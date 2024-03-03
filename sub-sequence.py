def longest_common_subsequence(list1, list2):
    m, n = len(list1), len(list2)

    # Create a 2D table to store the lengths of LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the table in a bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if list1[i - 1] == list2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Recover the LCS itself
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if list1[i - 1] == list2[j - 1]:
            lcs.append(list1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Reverse the LCS to get the correct order
    lcs.reverse()
    return lcs

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 1, 3, 5]
result = longest_common_subsequence(list1, list2)
print("Longest Common Subsequence:", result)
