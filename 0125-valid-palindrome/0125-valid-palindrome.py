class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = "".join([x.lower() for x in list(s) if x.isalnum()])
        left = 0
        right = len(res)-1
        for i in range(len(res)):
            if res[left] != res[right]:
                return False
            else:
                left +=1
                right -= 1
        return True