class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq ={}
        count = 0
        for i in nums :
            if i in freq:
                freq[i]+=1
            else : 
                freq[i]=1
        for i in freq:
            if freq[i] == 1:
                count += i
        return count


                    