from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if not nums or k == 0:
            return []
        
        result = []
        dq = deque()  # Stores indices of elements
        
        for i in range(len(nums)):
            # Remove indices that are out of the current window bounds
            if dq and dq[0] < i - k + 1:
                dq.popleft()
                
            # Remove elements smaller than the current element from the back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
                
            # Add the current element's index
            dq.append(i)
            
            # The first window finishes at index k - 1
            if i >= k - 1:
                result.append(nums[dq[0]])
                
        return result


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna