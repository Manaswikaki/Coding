class Solution:
    def romanToInt(self, s: str) -> int:
        # Map of Roman symbols to their integer values
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        for i in range(n):
            # Check if the current value is less than the next value
            if i < n - 1 and roman_map[s[i]] < roman_map[s[i+1]]:
                # Subtraction case (e.g., IV, IX, XL)
                total -= roman_map[s[i]]
            else:
                # Standard addition case
                total += roman_map[s[i]]
        
        return total


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna