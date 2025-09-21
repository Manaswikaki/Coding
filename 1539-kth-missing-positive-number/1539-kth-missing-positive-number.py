from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = 0
        prev = 0  # virtual previous value
        for x in arr:
            gap = x - prev - 1
            if missing + gap >= k:
                return prev + (k - missing)
            missing += gap
            prev = x
        return arr[-1] + (k - missing)