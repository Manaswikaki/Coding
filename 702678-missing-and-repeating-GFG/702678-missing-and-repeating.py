class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        
        # Sum of first n natural numbers
        s_expected = n * (n + 1) // 2
        p_expected = n * (n + 1) * (2 * n + 1) // 6
        
        s_actual = 0
        p_actual = 0
        
        for num in arr:
            s_actual += num
            p_actual += num * num
            
        # x - y
        diff_val = s_actual - s_expected
        # x^2 - y^2
        diff_sq_val = p_actual - p_expected
        
        # x + y = (x^2 - y^2) / (x - y)
        sum_val = diff_sq_val // diff_val
        
        repeating = (diff_val + sum_val) // 2
        missing = sum_val - repeating
        
        return [repeating, missing]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna