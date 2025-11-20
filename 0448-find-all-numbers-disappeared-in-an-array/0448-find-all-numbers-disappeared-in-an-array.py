class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        mydict={}
        l=[]
        for i in nums:
            mydict[i]=True
        for r in range(1,len(nums)+1):
            if r not in mydict:
                l.append(r)
        return l        
    
