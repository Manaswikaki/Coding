class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        ar=set(arr)
        if len(ar) ==1:
            return -1
        else:    
            a=max(ar)
            ar.remove(a)
            return max(ar)