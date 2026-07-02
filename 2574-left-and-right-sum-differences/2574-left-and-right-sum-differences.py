class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum=0
        lefttotal=[]
        rightsum=0
        righttotal=[]
        output=[]
        for i in range(len(nums)):
            lefttotal.append(leftsum)
            leftsum += nums[i]
    
        for j in range(len(nums)-1,-1,-1):
            righttotal.append(rightsum)
            rightsum+=nums[j]
        righttotal=list(reversed(righttotal))

        for i in range(len(lefttotal)):
            if len(lefttotal)==len(righttotal):
                nw=abs(lefttotal[i]-righttotal[i])
                output.append(nw)
        return output