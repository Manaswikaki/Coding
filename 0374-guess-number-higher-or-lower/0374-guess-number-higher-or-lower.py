# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        
        while low <= high:
            # Calculate middle point
            mid = low + (high - low) // 2
            res = guess(mid)
            
            if res == 0:
                return mid
            elif res == -1:
                # Target is lower, move high pointer
                high = mid - 1
            else:
                # Target is higher, move low pointer
                low = mid + 1
                
        return -1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna