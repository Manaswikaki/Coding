class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        summ = 0
        n = len(s)
        i = 0
        while i < n:
            # Check if the current value is less than the next one
            if i + 1 < n and d[s[i]] < d[s[i+1]]:
                summ += d[s[i+1]] - d[s[i]] # Add the difference
                i += 2 # Skip the next character as it's already handled
            else:
                summ += d[s[i]] # Add the current character's value
                i += 1
        return summ