class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip() # 1. Remove leading whitespace
        if not s:
            return 0
        
        sign = 1
        i = 0
        
        # 2. Check for sign
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
            
        res = 0
        # 3. Convert digits
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
            
        res *= sign
        
        # 4. Handle 32-bit integer clamping
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
            
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna