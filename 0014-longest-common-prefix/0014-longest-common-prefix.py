class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Start by assuming the first word is the prefix
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            # While the current word doesn't start with the prefix
            while not strs[i].startswith(prefix):
                # Shorten the prefix by one character from the end
                prefix = prefix[:-1]
                
                # If prefix becomes empty, there's no common prefix
                if not prefix:
                    return ""
        
        return prefix


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna