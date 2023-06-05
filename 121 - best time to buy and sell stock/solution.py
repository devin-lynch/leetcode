# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP

Solution().maxProfit([0,2,1,2,1,0,1,2])

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         l = 0
#         r = 1
#         profit = 0
#         for p in prices:
#             print(l, r)
#             if r < len(prices):
#                 if p < prices[l]:
#                     l = prices.index(p)
#                 if prices[l] > prices[r]:
#                     l, r = l + 1, r + 1
#                 else:
#                     if prices[r] - prices[l] > profit:
#                         profit = prices[r] - prices[l]
#                     r += 1
#             print(profit)
#         return profit

# Solution().maxProfit([0,2,1,2,1,0,1,2])


# init solutions:

# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         diff = 0
#         for p in prices:
#             for j in range(prices.index(p) + 1, len(prices)):
#                 # print(p)
#                 if prices[j] - p > diff:
#                     diff = prices[j] - p
#                     print(diff)
#         return diff

                

# Solution().maxProfit([4, 2, 5 ,9])

# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         diff = 0
#         for p in prices:
#             for j in prices:
#                 print(prices.index(j), prices.index(p))
#                 if prices.index(j) <= prices.index(p):
#                     continue
#                 if j - p > diff:
#                     diff = j - p
#                     print(diff)
#         return diff

                

# Solution().maxProfit([4, 2, 5 ,9])
