#Best time to Buy and sell stocks
prices = [7,1,5,3,6,4]
#output = 5

def maxProfit(prices:list[int])-> int:
    l = 0
    r = 1
    maxProfit = 0
    while r<len(prices):
        if prices[l]<prices[r]: #buy price is less than sell price
            profit = prices[r]-prices[l]
            maxProfit = max(profit, maxProfit)
        else:
            l = r
        r+= 1
    return maxProfit
#Time COmplexity: O(n)
#Space Complexity : O(1)
