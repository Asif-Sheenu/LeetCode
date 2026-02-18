class Solution:
    def reverseDegree(self, s: str) -> int:
        product=0
        for i in range(len (s)):
            index= i +1
            rev_ind= 26-(ord(s[i])-ord('a'))
            product+= index*rev_ind
        return(product)            