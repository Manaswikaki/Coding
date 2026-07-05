class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: Get the XOR sum of the two unique numbers
        xor_all = 0
        for n in nums:
            xor_all ^= n
        
        # Step 2: Isolate the rightmost set bit
        # This bit is different between the two target numbers
        diff_bit = xor_all & -xor_all
        
        # Step 3: Partition numbers into two groups and XOR
        a, b = 0, 0
        for n in nums:
            if n & diff_bit:
                a ^= n
            else:
                b ^= n
                
        return [a, b]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna