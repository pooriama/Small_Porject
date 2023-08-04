def buy_sell_stock(A):
    min_price = float("inf")
    max_profit = 0

    for price in A:
        max_price_profit = price - min_price
        min_price = min(price, min_price)
        max_profit = max(max_price_profit, max_profit)
    return max_profit


A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(buy_sell_stock(A))




def buy_sell_stock(A):
    max_profit,min_so_far=0,float("inf")

    for i in range(0,len(A)):
        max_profit=max(max_profit,(A[i]-min_so_far))
        min_so_far=min(min_so_far,A[i])
