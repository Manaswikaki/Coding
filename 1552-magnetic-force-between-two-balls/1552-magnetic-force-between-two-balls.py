class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        # Sort positions to allow sequential placement checking
        position.sort()
        
        # Helper function to check if we can place 'm' balls with at least 'distance' apart
        def canPlace(distance: int) -> bool:
            count = 1  # Place the first ball in the first basket
            last_pos = position[0]
            
            for i in range(1, len(position)):
                if position[i] - last_pos >= distance:
                    count += 1
                    last_pos = position[i]  # Update the position of the last placed ball
                    if count >= m:
                        return True
            return False

        # Binary search range
        low = 1
        high = position[-1] - position[0]
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            
            if canPlace(mid):
                ans = mid      # mid is a valid minimum force, save it
                low = mid + 1  # Try to find a larger maximum minimum force
            else:
                high = mid - 1 # Reduce the target distance
                
        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna