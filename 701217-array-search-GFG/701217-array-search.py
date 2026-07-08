class Solution:
    def search(self, arr, x):
        # Iterate through the array using its length
        for i in range(len(arr)):
            # Check if the element at index i is equal to x
            if arr[i] == x:
                return i
        
        # If the element is not found after checking the whole array
        return -1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna