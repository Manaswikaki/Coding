class Solution:
    def aggressiveCows(self, arr, k):
        # Step 1: Sort the stall positions
        arr.sort()
        
        # Step 2: Define the search space for the distance
        low = 1
        high = arr[-1] - arr[0]
        ans = 0
        
        # Helper function to check if a minimum distance 'mid' is possible
        def canPlaceCows(mid):
            count = 1  # Place the first cow in the first stall
            last_position = arr[0]
            
            for i in range(1, len(arr)):
                if arr[i] - last_position >= mid:
                    count += 1
                    last_position = arr[i]  # Place next cow here
                    
                if count >= k:
                    return True
            return False

        # Step 3: Binary search for the maximum minimum distance
        while low <= high:
            mid = (low + high) // 2
            
            if canPlaceCows(mid):
                ans = mid       # 'mid' is a valid distance, save it
                low = mid + 1   # Try to find a larger minimum distance
            else:
                high = mid - 1  # 'mid' is too large, reduce distance
                
        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna