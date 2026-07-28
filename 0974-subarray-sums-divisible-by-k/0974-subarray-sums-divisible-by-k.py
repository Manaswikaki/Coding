class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Dictionary to store the frequency of remainders
        # Base case: a prefix sum of 0 has a remainder of 0, seen 1 time initially
        remainder_count = {0: 1}
        
        running_sum = 0
        total_subarrays = 0
        
        for num in nums:
            running_sum += num
            # Get positive remainder
            remainder = running_sum % k
            
            # If the remainder has been seen before, add its frequency to total
            if remainder in remainder_count:
                total_subarrays += remainder_count[remainder]
                remainder_count[remainder] += 1
            else:
                remainder_count[remainder] = 1
                
        return total_subarrays


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna