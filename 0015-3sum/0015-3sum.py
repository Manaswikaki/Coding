class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Sort the array to use the two-pointer technique
        nums.sort()
        res = []
        length = len(nums)
        
        for i in range(length - 2):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Optimization: If the smallest possible triplet is > 0, break
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
                
            # Optimization: If the largest possible triplet with nums[i] is < 0, skip
            if nums[i] + nums[-2] + nums[-1] < 0:
                continue
            
            # Initialize two pointers
            left = i + 1
            right = length - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Skip duplicate values for the second element
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
                    # Skip duplicate values for the third element
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif current_sum < 0:
                    left += 1  # Sum is too small, move left pointer to increase sum
                else:
                    right -= 1 # Sum is too large, move right pointer to decrease sum
                    
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna