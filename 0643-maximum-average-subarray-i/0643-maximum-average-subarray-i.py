class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = sum(nums[:k])
        total=summ/k

        for i in range(k,len (nums)):
            summ += nums[i] 
            summ-= nums[i-k]
            total = max(total,summ/k)
        return (total)     