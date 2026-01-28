class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        ind= max(nums)
        sortednum=sorted(nums)

        for i in range (len (nums)):
            if (sortednum[-2]*2)<=ind:
                return nums.index(ind)
        return -1
