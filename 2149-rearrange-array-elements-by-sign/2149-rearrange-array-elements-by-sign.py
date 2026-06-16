class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Initialize the result array with zeros
        ans = [0] * len(nums)
        
        # Pointers for the next positive and negative positions
        pos_idx = 0
        neg_idx = 1
        
        for num in nums:
            if num > 0:
                # Place positive number at current positive index
                ans[pos_idx] = num
                pos_idx += 2
            else:
                # Place negative number at current negative index
                ans[neg_idx] = num
                neg_idx += 2
                
        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna