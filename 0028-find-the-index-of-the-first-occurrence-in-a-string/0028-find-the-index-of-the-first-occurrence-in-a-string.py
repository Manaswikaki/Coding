class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # If needle is empty, per problem statement return 0
        if not needle:
            return 0
        # Simple approach: find the first occurrence of needle in haystack
        idx = haystack.find(needle)
        return idx