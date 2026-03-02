from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            count = 0
            for j in nums:
                if j < i:
                    count += 1
            res.append(count)
        return res