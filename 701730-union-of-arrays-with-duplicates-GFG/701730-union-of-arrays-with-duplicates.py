class Solution:
    def findUnion(self, a, b):
        # Use a set to collect distinct elements from both arrays
        union_set = set(a) | set(b)
        # Return as a list (order can be arbitrary; driver prints sorted)
        return list(union_set)