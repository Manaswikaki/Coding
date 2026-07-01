class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_map = {}
        count = 0
        
        # Step 1: Pre-calculate sums of the first two arrays
        for i in nums1:
            for j in nums2:
                current_sum = i + j
                sum_map[current_sum] = sum_map.get(current_sum, 0) + 1
        
        # Step 2: Find complements in the remaining two arrays
        for k in nums3:
            for l in nums4:
                target = -(k + l)
                if target in sum_map:
                    count += sum_map[target]
                    
        return count


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna