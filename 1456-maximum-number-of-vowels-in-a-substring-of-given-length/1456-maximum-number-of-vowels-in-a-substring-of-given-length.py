class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        window=s[:k]
        count=0
        for i in range(k):
            if s[i] in "aeiou":
                count +=1
        best=count
        for i in range(k,len(s)):
            if s[i] in "aeiou":
                count +=1
            if s[i-k] in "aeiou":
                count -=1
            best= max(best,count)
        return best      
        
