from collections import Counter
class Solution:
    def majorityElement(self, arr):
        #code here
        cou=Counter(arr)
        size=len(arr)
        val=size/2
        res=True
        re=0
        for i in arr:
            if cou[i] > val:
                re=i
                res=True
                break
            else:
                res=False
        if res:
            return re
        else:
            return -1