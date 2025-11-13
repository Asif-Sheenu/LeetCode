class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = [i for i in nums if nums.count(i)==1]
        return (result[0])