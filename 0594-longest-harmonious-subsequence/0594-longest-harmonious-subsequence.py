from collections import Counter

class Solution:
    def findLHS(self, nums: list[int]) -> int:
        # Count the frequency of each number
        counts = Counter(nums)
        max_length = 0
        
        # Iterate through the unique numbers in the array
        for x in counts:
            # Check if there is a number exactly 1 greater than the current number
            if x + 1 in counts:
                # The length of the harmonious subsequence for (x, x+1)
                current_length = counts[x] + counts[x + 1]
                max_length = max(max_length, current_length)
                
        return max_length
