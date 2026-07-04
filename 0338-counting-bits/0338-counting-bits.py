class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize the result array with 0s
        ans = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # ans[i] is ans[i >> 1] plus 1 if i is odd
            ans[i] = ans[i >> 1] + (i & 1)
            
        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna