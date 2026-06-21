class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        
        while left < right:
            # Swap characters at left and right pointers
            s[left], s[right] = s[right], s[left]
            
            # Move pointers toward the center
            left += 1
            right -= 1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna