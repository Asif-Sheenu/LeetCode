class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        average=[]
        for i in range(len(nums)//2):
            minVal=nums.pop(0)
            maxVal=nums.pop()
            average.append((minVal+maxVal)/2)
        return min(average)    
