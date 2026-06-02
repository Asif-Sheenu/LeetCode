class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxvalue=float ('-inf')
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j] :
                    maxvalue= max(maxvalue,(nums[j]-nums[i]))
        if maxvalue != float('-inf'):  
            return maxvalue          
        else:
            return -1  