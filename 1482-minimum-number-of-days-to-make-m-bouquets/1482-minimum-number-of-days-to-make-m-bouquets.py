class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        # Edge case: Not enough flowers available in total
        if m * k > len(bloomDay):
            return -1
        
        def canMake(days: int) -> bool:
            bouquets = 0
            flowers = 0
            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0 # Reset consecutive counter if flower hasn't bloomed
            return bouquets >= m

        # Binary search range
        low = min(bloomDay)
        high = max(bloomDay)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if canMake(mid):
                ans = mid       # Track the valid minimum day
                high = mid - 1  # Try to find a smaller day
            else:
                low = mid + 1   # Increase the day threshold

        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna