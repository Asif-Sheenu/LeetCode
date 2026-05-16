class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen =0
        maxi=""
        for i in range(len(s)):
            while s[i] in maxi:
                maxi=maxi[1::]      
            if s[i] not in maxi:
                maxi+=s[i]
            maxlen= max(maxlen, len(maxi))  
        return maxlen 

