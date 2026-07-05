class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones = 0
        twos = 0
        
        for num in nums:
            # 'ones' tracks bits that have appeared once
            ones = (ones ^ num) & ~twos
            # 'twos' tracks bits that have appeared twice
            twos = (twos ^ num) & ~ones
            
        return ones


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna