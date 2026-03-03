from collections import Counter
class Solution:
    def countFreq(self, arr, target):
        # code here
        a=Counter(arr)
        return a[target]