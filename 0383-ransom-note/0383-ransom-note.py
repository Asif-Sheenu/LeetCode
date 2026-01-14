class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = {}
        for m in magazine:
            if m in freq:
                freq[m]+=1
            else :
                freq[m] = 1

        for i in ransomNote :
            if i in freq and freq[i]>0:
                freq[i]-=1
            else:
                return False  
        return True                

             