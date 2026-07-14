import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search range for speed k
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            total_hours = 0
            
            for pile in piles:
                # Calculate hours for current pile at speed mid
                total_hours += math.ceil(pile / mid)
            
            if total_hours <= h:
                # Speed is sufficient, try to find a smaller one
                right = mid
            else:
                # Speed is too slow, must increase it
                left = mid + 1
                
        return left


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna