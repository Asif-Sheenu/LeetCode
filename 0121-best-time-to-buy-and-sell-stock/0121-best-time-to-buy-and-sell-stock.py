class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit= 0
        mini = prices[0]    
        for i in prices:
            if i < mini:
                mini=i
            profit= max(profit,(i - mini))
        return (profit) 
        
    
       