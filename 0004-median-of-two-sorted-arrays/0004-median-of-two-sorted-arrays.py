from typing import List
import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        low, high = 0, m

        while True:
            i = (low + high) // 2
            j = half - i

            L1 = nums1[i - 1] if i > 0 else float('-inf')
            L2 = nums2[j - 1] if j > 0 else float('-inf')
            R1 = nums1[i] if i < m else float('inf')
            R2 = nums2[j] if j < n else float('inf')

            if L1 <= R2 and L2 <= R1:
                if total % 2 == 1:
                    return min(R1, R2)
                else:
                    return (max(L1, L2) + min(R1, R2)) / 2.0
            elif L1 > R2:
                high = i - 1
            else:  # L2 > R1
                low = i + 1