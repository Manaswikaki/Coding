class Solution:
    def commonElements(self, a, b):
        a.sort()
        b.sort()
        res = []
        i, j = 0, 0
        
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                res.append(a[i])
                i += 1
                j += 1
            elif a[i] < b[j]:
                i += 1
            else:
                j += 1
        return res
