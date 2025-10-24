from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        l5 = 0
        l10 = 0
        l20 = 0

        for n in bills:
            if n == 5:
                l5 += 1

            elif n == 10:
                if l5 == 0:  
                    return False
                l5 -= 1
                l10 += 1

            elif n == 20:
                if l10 > 0 and l5 > 0:  
                    l10 -= 1
                    l5 -= 1
                elif l5 >= 3:         
                    l5 -= 3
                else:
                    return False

        return True
