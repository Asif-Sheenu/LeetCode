class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        sl=list(s)
        result=[] 
        final=[]
        for i in sl :
            if i.isalpha():
                result.append(i)
        print (result)  

        for i in sl :
            if i.isalpha():
                final.append(result.pop())
            else:
                final.append(i)
        return ("".join(final))   
                