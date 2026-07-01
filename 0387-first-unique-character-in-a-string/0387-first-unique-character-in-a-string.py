class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        
        # Build frequency map
        for char in s:
            count[char] = count.get(char, 0) + 1
            
        # Find the first character with a count of 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        
        return -1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna