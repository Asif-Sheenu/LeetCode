class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
         result = []
         for n in candies:
            if n + extraCandies >= max(candies):
             print (result.append(True))
            else:
             print (result.append(False))
         
         return result     