class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        # 1. Initialize two candidates and their counts
        cand1, cand2 = None, None
        count1, count2 = 0, 0
        
        # 2. Voting process
        for n in nums:
            if n == cand1:
                count1 += 1
            elif n == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = n, 1
            elif count2 == 0:
                cand2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1
        
        # 3. Verification process
        result = []
        n_size = len(nums)
        for cand in [cand1, cand2]:
            if cand is not None and nums.count(cand) > n_size // 3:
                result.append(cand)
                
        return result


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna