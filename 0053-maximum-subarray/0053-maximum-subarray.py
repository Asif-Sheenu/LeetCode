class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result =nums[0]
        current=nums[0]
        for i in range (1,len(nums)):
            if nums[i] > current+ nums[i]:
                current= nums[i]
            else:
                current = current +nums[i]
            if current > result:
                result =current
        return result         