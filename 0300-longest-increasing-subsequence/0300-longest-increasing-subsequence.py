import bisect

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # sub will store the smallest tail of all increasing subsequences found so far
        sub = []
        
        for num in nums:
            # Find the index of the first element >= num
            idx = bisect.bisect_left(sub, num)
            
            # If num is greater than all elements in sub, append it
            if idx == len(sub):
                sub.append(num)
            # Otherwise, replace the element at idx with num to maintain a smaller tail
            else:
                sub[idx] = num
                
        return len(sub)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna