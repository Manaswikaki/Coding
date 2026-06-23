from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # defaultdict handles missing keys automatically
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the string to use as a unique key for all its anagrams
            # Sorted returns a list, so we join it back into a string
            sorted_key = "".join(sorted(s))
            anagram_map[sorted_key].append(s)
            
        # Return only the grouped values
        return list(anagram_map.values())


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna