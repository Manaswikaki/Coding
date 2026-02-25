class Solution:
    def binarysearch(self, arr, k):
        # Code Here
        for i in range(0,len(arr)+1):
            if k not in arr:
                return -1
                break
            else:
                return arr.index(k)
        