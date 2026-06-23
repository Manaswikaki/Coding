class Solution:
    def reverseWords(self, s: str) -> str:
        # split() without arguments splits by any whitespace and discards empty strings
        words = s.split()
        
        # Reverse the list of words
        words.reverse()
        
        # Join the words with a single space
        return " ".join(words)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna