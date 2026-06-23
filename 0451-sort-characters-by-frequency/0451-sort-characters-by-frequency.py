from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # 1. Count frequencies of each character
        counts = Counter(s)
        
        # 2. Sort characters by frequency in descending order
        # Counter.most_common() returns a list of (char, count) tuples 
        # sorted by count automatically.
        sorted_chars = counts.most_common()
        
        # 3. Build the resulting string
        result = []
        for char, count in sorted_chars:
            result.append(char * count)
            
        return "".join(result)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna