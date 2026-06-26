class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        # Combine string with its reverse using a separator
        combined = s + "#" + s[::-1]
        
        # Build KMP table (Partial Match Table)
        n = len(combined)
        pi = [0] * n
        for i in range(1, n):
            j = pi[i - 1]
            while j > 0 and combined[i] != combined[j]:
                j = pi[j - 1]
            if combined[i] == combined[j]:
                j += 1
            pi[i] = j
        
        # pi[-1] is the length of the longest palindromic prefix
        longest_palindrome_prefix_len = pi[-1]
        
        # Suffix to reverse and add to the front
        suffix_to_add = s[longest_palindrome_prefix_len:][::-1]
        
        return suffix_to_add + s


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna