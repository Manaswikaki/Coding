class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1] * length
        
        # Step 1: Calculate prefix products
        # answer[i] contains the product of all elements to the left of i
        prefix = 1
        for i in range(length):
            answer[i] = prefix
            prefix *= nums[i]
            
        # Step 2: Calculate suffix products and combine
        # Multiply answer[i] with the product of all elements to the right of i
        suffix = 1
        for i in range(length - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
            
        return answer


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna