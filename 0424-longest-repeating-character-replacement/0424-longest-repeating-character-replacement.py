class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_length = 0
        max_count = 0
        left = 0
        
        for right in range(len(s)):
            # Add the current character to the frequency map
            count[s[right]] = 1 + count.get(s[right], 0)
            
            # Track the max frequency of any character seen so far in the current window
            max_count = max(max_count, count[s[right]])
            
            # If the current window is invalid, shrink it from the left
            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1
                
            # Update the maximum valid window length found
            max_length = max(max_length, right - left + 1)
            
        return max_length


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna