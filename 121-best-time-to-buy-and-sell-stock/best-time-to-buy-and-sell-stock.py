class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        

        #brute force 
        maxp = 0; 
        for i in range(0,len(prices)): 
            for j in range(i+1,len(prices)):
                if prices[j]-prices[i]>0: 
                    if prices[j]-prices[i]>maxp:
                        maxp = prices[j]-prices[i]
                else: 
                    break;


        return maxp
