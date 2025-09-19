from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Traverse from last digit
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  # carry over if digit was 9
        
        # If all were 9s, e.g., [9,9,9] -> [1,0,0,0]
        return [1] + digits
