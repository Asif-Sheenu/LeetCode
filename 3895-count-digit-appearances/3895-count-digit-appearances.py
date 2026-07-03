class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count=0
        num = "".join(map(str, nums))
        for i in num:
            if digit == int(i) :
                count+=1
        return count   