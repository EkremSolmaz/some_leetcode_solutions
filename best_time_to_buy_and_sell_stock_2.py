from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        buys = []
        sells = []
        profit = 0

        if prices[0] < prices[1]:
            buys.append(prices[0])

        for i in range(1, len(prices)-1):
            if prices[i-1] < prices[i] >= prices[i+1]:
                if buys:
                    #sell point
                    sells.append(prices[i])
            elif prices[i-1] >= prices[i] < prices[i+1]:
                #buy point
                buys.append(prices[i])

        if prices[-1] > prices[-2]:
            sells.append(prices[-1])

        for i in range(len(buys)):
            profit -= buys[i]
            profit += sells[i]

        return profit

print(Solution().maxProfit(prices = [7,1,5,3,6,4]))
print(Solution().maxProfit(prices = [1,2,3,4,5]))
print(Solution().maxProfit(prices = [7,6,4,3,1]))
        
