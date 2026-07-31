class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        
        # If s1 is longer than s2, s2 cannot contain a permutation of s1
        if len1 > len2:
            return False
            
        # Initialize frequency counts for lowercase English letters (26 choices)
        count1 = [0] * 26
        count2 = [0] * 26
        
        # Populate the initial frequencies for s1 and the first window of s2
        for i in range(len1):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
            
        # If the first window matches, we found a permutation immediately
        if count1 == count2:
            return True
            
        # Slide the window across s2
        for i in range(len1, len2):
            # Add the new character entering the window from the right
            count2[ord(s2[i]) - ord('a')] += 1
            # Remove the old character leaving the window from the left
            count2[ord(s2[i - len1]) - ord('a')] -= 1
            
            # Check if the updated window matches s1's frequency
            if count1 == count2:
                return True
                
        return False


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna