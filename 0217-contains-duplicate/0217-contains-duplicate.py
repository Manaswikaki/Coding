class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=set(nums)
        l=len(nums)
        le=len(a)
        if l == le:
            return False
        else:
            return True   