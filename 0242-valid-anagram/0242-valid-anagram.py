class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_t = {}
        for i in t:
            if i in freq_t:
                freq_t[i]+=1
            else :
                freq_t[i]=1

        freq_s ={}
        for so in s:
            if so in freq_s:
                freq_s[so]+=1
            else :
                freq_s[so]=1

        return freq_s == freq_t

        # for ana in s:
        #     if ana in freq or freq<0:
        #         freq[ana]-=1
        #     else:
        #         return False
        #     return True                    