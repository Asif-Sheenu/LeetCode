class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_t = {}
        for i in t:
            freq_t[i] = freq_t.get(i,0)+1

        freq_s ={}
        for so in s:
            freq_s[so] = freq_s.get(so,0)+1

        return freq_s == freq_t

        # for ana in s:
        #     if ana in freq or freq<0:
        #         freq[ana]-=1
        #     else:
        #         return False
        #     return True                    