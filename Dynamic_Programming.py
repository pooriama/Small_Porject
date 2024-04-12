n = 7
dp = [-1 for i in range(n + 1)]
def solve(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    dp[n] = solve(n - 5) + solve(n - 3) + solve(n - 1)
    return dp[n]
print("Sum to ",{n},solve(n),"\n")



n = 5
ans = [-1] * (n + 1)
def fibo(n):
    if n <= 1:
        return n
    if ans[n] != -1:
        return ans[n]
    ans[n] = fibo(n - 1) + fibo(n - 2)
    return ans[n]


print("Fibonachi for ",{n},fibo(5))
