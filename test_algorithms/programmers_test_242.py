def max_profit(gold_prices):
    if len(gold_prices) < 2:
        return 0
    
    # Initialize variables
    buy_day = 0
    sell_day = 1
    max_profit = 0
    
    while sell_day < len(gold_prices):
        if gold_prices[sell_day] <= gold_prices[buy_day]:
            # If the price on the sell day is less than or equal to the price on the buy day,
            # update the buy day to the sell day
            buy_day = sell_day
        else:
            # If the price on the sell day is greater than the price on the buy day,
            # calculate the profit and update the sell day
            profit = gold_prices[sell_day] - gold_prices[buy_day]
            if profit > max_profit:
                max_profit = profit
            sell_day += 2
    
    return max_profit

print(max_profit([2,5,1,3,4]))
print(max_profit([7, 2, 5, 6, 1, 4, 2, 8]))