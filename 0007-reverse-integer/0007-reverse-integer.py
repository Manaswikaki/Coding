class Solution:
    def reverse(self, x: int) -> int:
        u = 0
        a = x
        
        # Safely get the absolute value as an integer
        x = abs(x)
        
        # This loop now safely terminates because x is always positive
        while x != 0:
            r = x % 10
            u = u * 10 + r
            x = x // 10
            
        # Reapply the negative sign if the original input was negative
        if a < 0:
            u = -u    
            
        # 32-bit signed integer overflow check
        if u < -2**31 or u > 2**31 - 1:
            return 0
            
        return u

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna