class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Converting to a set makes "in" lookups O(1) instead of O(n)
        num_set = set(nums) 
        n = len(nums)
        
        for i in range(1, n + 2): # Range up to n+1
            if i not in num_set:
                return i
 