class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        p_count = {}
        s_count = {}
        
        # Initialize counts for string p and the first window of string s
        for i in range(len(p)):
            p_count[p[i]] = p_count.get(p[i], 0) + 1
            s_count[s[i]] = s_count.get(s[i], 0) + 1
            
        res = []
        if p_count == s_count:
            res.append(0)
            
        # Slide the window across string s
        left = 0
        for right in range(len(p), len(s)):
            # Add the new character to the window
            s_count[s[right]] = s_count.get(s[right], 0) + 1
            
            # Remove the oldest character from the window
            s_count[s[left]] -= 1
            if s_count[s[left]] == 0:
                del s_count[s[left]]
                
            left += 1
            
            # If counts match, an anagram is found
            if s_count == p_count:
                res.append(left)
                
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna