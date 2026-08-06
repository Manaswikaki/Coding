class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Maps each number in nums2 to its next greater element
        next_greater = {}
        stack = []
        
        # Traverse nums2 to find the next greater element for every number
        for num in nums2:
            # Maintain a monotonic decreasing stack
            while stack and stack[-1] < num:
                smaller_num = stack.pop()
                next_greater[smaller_num] = num
            stack.append(num)
            
        # For any elements left in the stack, there is no greater element
        # (Python's dict.get() can default to -1 for these)
        
        # Build the result array for nums1 using the map
        return [next_greater.get(num, -1) for num in nums1]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna