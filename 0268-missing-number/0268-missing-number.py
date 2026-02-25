class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res=0
        n=max(nums)
        for i in range(0,n+2):
            if i in nums:
                pass
            else:
                return i
                break    