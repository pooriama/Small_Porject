def LCS(str1, str2, m, n):
    if m == 0:
        return 0
    if n == 0:
        return 0
    if str1[m - 1] == str2[n - 1]:
        return 1 + LCS(str1, str2, m - 1, n - 1)
    return max(LCS(str1, str2, m, n - 1), LCS(str1, str2, m - 1, n))


str1 = "AGGTAB"
str2 = "GXTXAYB"
print("Length of LCS is ", LCS(str1, str2, len(str1), len(str2)))
