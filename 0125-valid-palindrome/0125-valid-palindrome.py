class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers at the start and end of the string
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters from the left
            if not s[left].isalnum():
                left += 1
            # Skip non-alphanumeric characters from the right
            elif not s[right].isalnum():
                right -= 1
            else:
                # Compare characters (case-insensitive)
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
                
        return True


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna