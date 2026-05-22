class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = sum(nums[:k])
        totalavg=summ/k

        for i in range(k,len (nums)):
            summ += nums[i] 
            summ-= nums[i-k]
            totalavg = max(totalavg,summ/k)
        return (totalavg)     