class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a=set(nums)
        if len(a) <3:
            return max(a)
        a.remove(max(a))
        a.remove(max(a)) 
        return max(a)   