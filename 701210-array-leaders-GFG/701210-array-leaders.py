class Solution:
    def leaders(self, arr):
        # If the input could be empty (though constraints say at least 1), handle gracefully
        if not arr:
            return []

        n = len(arr)
        leaders_rev = []
        max_right = float('-inf')

        # Scan from right to left
        for i in range(n - 1, -1, -1):
            if arr[i] >= max_right:
                leaders_rev.append(arr[i])
                max_right = arr[i]

        # Reverse to get left-to-right order
        return leaders_rev[::-1]