class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        result=[]
        flat = [i for arr in grid for i in arr]
        freq={}
        for i in range(len(flat)):
            if flat[i] in freq :
                freq[flat[i]]+=1
            else :
                freq[flat[i]]=1

        for k,v in freq.items():
            if v > 1:
                result.append(k)

        for i in range(1,len(flat)+1):
            if i not in flat:
                result.append(i)

        return result        