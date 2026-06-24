class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start, end = 0, 0
        
        for i in range(len(s)):
            # Check for odd-length palindromes (center is a character)
            len1 = self.expandAroundCenter(s, i, i)
            # Check for even-length palindromes (center is between characters)
            len2 = self.expandAroundCenter(s, i, i + 1)
            
            # Take the maximum length found at this center
            max_len = max(len1, len2)
            
            # Update the start and end indices of the longest palindrome
            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start : end + 1]

    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        # Expand as long as pointers are in bounds and characters match
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        # Return the length of the palindrome found
        return right - left - 1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna