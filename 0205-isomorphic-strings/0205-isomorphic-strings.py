class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}

        for char_s, char_t in zip(s, t):
            # Check if mapping from s to t is consistent
            if char_s in mapST and mapST[char_s] != char_t:
                return False
            
            # Check if mapping from t to s is consistent
            if char_t in mapTS and mapTS[char_t] != char_s:
                return False
            
            # Establish mappings
            mapST[char_s] = char_t
            mapTS[char_t] = char_s
            
        return True


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna