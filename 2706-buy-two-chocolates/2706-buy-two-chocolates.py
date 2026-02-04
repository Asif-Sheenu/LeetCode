class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        wallet = money
        org_money=money
        count=0
        prices.sort()
        for i in prices:
            if i <= wallet and count < 2:
                money-=i
                wallet = money
                count+=1
            else:
                break
        if count<2:
            return (org_money)         
        return wallet    

