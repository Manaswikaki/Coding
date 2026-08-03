from collections import Counter

class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        # Helper function to find count of subarrays with AT MOST 'at_most_k' distinct elements
        def get_at_most_k(at_most_k: int) -> int:
            if at_most_k == 0:
                return 0
            
            count = 0
            left = 0
            freq = Counter()
            
            for right in range(len(nums)):
                # Add the current number to our sliding window
                freq[nums[right]] += 1
                
                # Shrink window from the left if distinct elements exceed target limit
                while len(freq) > at_most_k:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        del freq[nums[left]]
                    left += 1
                
                # The number of valid subarrays ending at 'right' index is (right - left + 1)
                count += (right - left + 1)
                
            return count

        # Exactly K = At Most K minus At Most (K - 1)
        return get_at_most_k(k) - get_at_most_k(k - 1)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna