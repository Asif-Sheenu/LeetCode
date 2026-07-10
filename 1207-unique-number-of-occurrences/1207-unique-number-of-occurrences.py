class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq={}

        for i in arr:
            if i in freq:
                freq[i]+=1
            else :
                freq[i]=1
        result= False
        freq1=set(freq.values())
        freq2=list(freq.values())
        if len(freq1)== len(freq2):
            result=True
    
        return result          