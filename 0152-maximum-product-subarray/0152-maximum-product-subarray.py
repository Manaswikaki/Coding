class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        res = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]
        
        for i in range(1, len(nums)):
            n = nums[i]
            
            # If n is negative, the max becomes the min and vice versa
            if n < 0:
                cur_max, cur_min = cur_min, cur_max
            
            cur_max = max(n, cur_max * n)
            cur_min = min(n, cur_min * n)
            
            res = max(res, cur_max)
            
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna