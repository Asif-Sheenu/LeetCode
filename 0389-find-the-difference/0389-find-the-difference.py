class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
            freq ={}
            for i in s:
                if i in freq:
                    freq[i]+=1
                else:
                    freq[i]=1
            for n in t:
                if n in freq and freq[n]>0:
                    freq[n] -= 1
                else : 
                    return (n)             
       



            
        