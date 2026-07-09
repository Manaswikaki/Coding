class Solution:
    def findIndex(self, arr, key):
        start_index = -1
        end_index = -1
        
        # Iterate through the array to find the first and last occurrences
        for i in range(len(arr)):
            if arr[i] == key:
                if start_index == -1:
                    start_index = i  # Found the first occurrence
                end_index = i        # Update last occurrence as we go
                
        return [start_index, end_index]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna