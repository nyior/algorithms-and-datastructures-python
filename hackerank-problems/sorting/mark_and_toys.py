"""
    Mark and Jane are very happy after having their first child. 
    Their son loves toys, so Mark wants to buy some. 
    There are a number of different toys lying in front of him, tagged with their prices. 
    Mark has only a certain amount to spend, and he wants to maximize the 
    number of toys he buys with this money. 
    Given a list of toy prices and an amount to spend, 
    determine the maximum number of gifts he can buy.

    Note Each toy can be purchased only once

    Example
    prices = [1,2,3,4]
    k=7

    The budget is  7 units of currency. 
    He can buy items that cost [1,2,3] for 6, or  [3,4] for 7  units. The maximum is 3 items.
"""

def maximum_toys(prices, k):
    total = 0
    counter = 0
    
    prices = sorted(prices)
    
    for i in prices:
        if (total+i) > k:
            return counter
        
        total += i
        counter += 1