import sys


def mincost(cost, m, n):
    if n < 0 or m < 0:
        return sys.maxsize
    elif (m == 0 and n == 0):
        return cost[m][n]
    return cost[m][n] + min(mincost(cost,m - 1, n), mincost(cost,m, n - 1), mincost(cost,m - 1, n - 1))


cost = [[1,2,3],
        [4,8,2],
        [1,5,3]]

print("Recursive way",mincost(cost,2,2))




memo = [[-1]*3 for i in range(3)]


def mincost_memoized(cost, m, n, memo):

    if m < 0  or n < 0 :
        return float("inf")
    if m == 0 and n == 0:
        return cost[m][n]
    if memo[m][n] != -1:
        return memo[m][n]

    memo[m][n] = cost[m][n] + min(mincost_memoized(cost, m - 1, n - 1, memo), mincost_memoized(cost, m, n - 1, memo),
                    mincost_memoized(cost, m - 1, n, memo))
    return memo[m][n]

print("Dynamic Programming memoization",mincost_memoized(cost,2,2,memo))



