class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minimum= prices [0]
        maxi=0
        profit= 0


        for i in prices:
            if minimum>i:
                minimum=i
            else:
                maxi= i - minimum
                if profit < maxi:
                    profit= maxi
        return (profit)
       