class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxvalue=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j] :
                    maxvalue.append(nums[j]-nums[i])
        if maxvalue:            
            return (max(maxvalue))
        else:
            return -1  