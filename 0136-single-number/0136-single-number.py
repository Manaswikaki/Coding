from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count=Counter(nums)
        a=set(nums)
        for i in a:
            if count[i]==1:
                return i