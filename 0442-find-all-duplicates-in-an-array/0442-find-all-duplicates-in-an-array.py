class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result =[]
        freq={}
        for i in nums :
            freq[i]=freq.get(i,0)+1

        for key,val in freq.items():
            if val>1:
                result.append(key) 

        return result           