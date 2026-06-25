class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_length = 0
        start = 0
        
        for end in range(len(s)):
            char = s[end]
            
            # If the character is a repeat and inside the current window
            if char in char_map and char_map[char] >= start:
                start = char_map[char] + 1
            
            # Update the latest index of the character
            char_map[char] = end
            
            # Update max_length if current window is larger
            max_length = max(max_length, end - start + 1)
            
        return max_length


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna