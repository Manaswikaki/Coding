import math

class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        def get_sum(divisor):
            # math.ceil(n / d) is equivalent to (n + d - 1) // d
            return sum((n + divisor - 1) // divisor for n in nums)

        low, high = 1, max(nums)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if get_sum(mid) <= threshold:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna