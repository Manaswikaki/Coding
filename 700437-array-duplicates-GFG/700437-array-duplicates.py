from collections import Counter
class Solution:
    def findDuplicates(self, arr):
        # code here
        cou=Counter(arr)
        res=[]
        for i in cou:
            if cou[i]>1:
                res.append(i)
        return res