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
