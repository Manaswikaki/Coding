from collections import Counter

class Solution:
    def isSubset(self, a, b):
        counts = Counter(a)
        
        for x in b:
            if counts[x] > 0:
                counts[x] -= 1
            else:
                return False
        
        return True