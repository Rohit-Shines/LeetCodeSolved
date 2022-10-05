# stocks logic-> identify the minimum value first
# mi =[0] max =[1] profit= ma-in

class Solution(object):
    def maxProfit(self, prices=[7, 1, 5, 3, 6, 4]):
        if len(prices) == 0: return 0  # breaking statement
        profit = 0; mi = prices[0] # 7 // which is the first number in this case
        for ma in prices[1:]:  # stating from 2nd index to end 1,5,3,6,4
            if ma < mi:  # 7<7 / 1< 7
                mi = ma  # mi =1/
            elif profit < (ma - mi):  # 0 < 7-7 /
                profit = ma - mi  # 7-7

        print("maximum price to buy",ma)
        print("minimum price to buy",mi)
        print("Profit of the stock ",profit)
        return
obj = Solution()
obj.maxProfit()