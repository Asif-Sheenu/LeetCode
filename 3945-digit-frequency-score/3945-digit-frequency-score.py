class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        freq={}
        for i in str(n):
            freq[i]=freq.get (i,0)+1
        output=0
        for k,v in freq.items():
            output+=int(k)*v
        return output    