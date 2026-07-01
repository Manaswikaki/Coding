from collections import Counter

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Optimization: Always iterate over the smaller array to save space
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
            
        # Step 1: Count frequencies of elements in nums1
        counts = Counter(nums1)
        res = []
        
        # Step 2: Iterate through nums2 and build the result
        for num in nums2:
            if counts[num] > 0:
                res.append(num)
                counts[num] -= 1
                
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna