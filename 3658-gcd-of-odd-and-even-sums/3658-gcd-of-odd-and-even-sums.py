class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # oddsum = sum([i*2+1 for i in range(n)])
        # evensum= sum([i*2 for i in range(1,n+1)])
        # biggest= max(oddsum,evensum)
        # result=[]
        # for i in range(1,biggest):
        #     if evensum % i == 0 and oddsum % i == 0:
        #         result.append(i)
        
        # return (max(result)) 
        return n