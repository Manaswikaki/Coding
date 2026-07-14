class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # The lowest possible capacity is the heaviest single package
        # The highest possible capacity is the sum of all packages
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            
            # Check if we can ship everything with 'mid' capacity
            current_weight = 0
            needed_days = 1
            for w in weights:
                if current_weight + w > mid:
                    needed_days += 1
                    current_weight = 0
                current_weight += w
            
            if needed_days <= days:
                # Capacity might be smaller, try left half
                right = mid
            else:
                # Capacity is too small, must increase
                left = mid + 1
                
        return left


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna