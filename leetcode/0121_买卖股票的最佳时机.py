
def func(prices: list[int]) -> int:
    if prices == sorted(prices, reverse=True):
        return 0

    max_profit = 0
    # for i in range(len(prices)):
    #     for j in range(i+1, len(prices)):
    #         m = 0
    #         if prices[i] < prices[j]:
    #             max_profit = max(max_profit, prices[j] - prices[i])
    l = prices.copy()
    for i in range(len(prices) - 1):
        l.pop(0)
        if prices[i] < max(l):
            max_profit = max(max_profit, max(l) - prices[i])
    return max_profit



print(func([7,1,5,3,6,4]))
print(func([7,5,4]))
