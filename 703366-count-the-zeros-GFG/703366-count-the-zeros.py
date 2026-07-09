class Solution:
    def countZeroes(self, arr):
        n = len(arr)
        
        # If the first element is 0, the entire array is 0s
        if arr[0] == 0:
            return n
        # If the last element is 1, there are no 0s
        if arr[n-1] == 1:
            return 0
            
        # Binary Search to find the index of the first '0'
        low = 0
        high = n - 1
        first_zero_index = -1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == 0:
                # Potential first zero, check left side
                first_zero_index = mid
                high = mid - 1
            else:
                # It's a 1, look to the right
                low = mid + 1
        
        # Total count is total length minus the index of the first zero
        return n - first_zero_index


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna