#Best Time To Buy And Sell Stock

# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one  transaction (i.e buy one and sell one share of the stock) design an algorithm  to find the maximum profit
# Note that you cannot sell a stock before you buy one

#Example Input: [7,1,5,3,6,4] , Output : 5
# Buy on day 2 (Price = 1) and sell on day 5 (price = 6) , Profit = 6 - 1 = 5. Not 7 - 1 = 6. Selling price need to be larger than by price
# L = Buy
# R = Sell

# Time: O(n)
# Memory: O(1)

#Code: 

class solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # Left is buying and Right is selling
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]: #Check if it profitable
                profit  = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r 
            r += l

        return maxP
